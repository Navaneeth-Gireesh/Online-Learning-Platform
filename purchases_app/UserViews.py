from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from courses_app.models import Course
from . UserForms import CoursesPurchasedForm
from . models import CoursesPurchased, CouponCode
from django.utils import timezone

# Create your views here.

# --------------------------- User Course Purchase ---------------------------

# User Buy Now
@login_required(login_url='/error_404/')
def buy_now(request, course_slug):
    selected_course = get_object_or_404(Course, slug = course_slug)
    context = {
        'selected_course' : selected_course
    }
    return render(request, 'Users/Buy_Now.html',context)

# Invalid Coupon Code
@login_required(login_url='/error_404/')
def invalid_coupon_code(request):
    return render(request, 'Users/Invalid_Coupon_Code.html')

# User Purchase Course
@login_required(login_url='/error_404/')
def user_purchase_course(request, course_slug):
    selected_course = get_object_or_404(Course, slug=course_slug)

    current_user = request.user
    if request.method == 'POST':
        entered_coupon = request.POST.get('coupon_code').strip()
        usage_count_check = CouponCode.objects.filter(code = entered_coupon, is_active = True).first()

        if usage_count_check:
            if (usage_count_check.usage_count >= usage_count_check.usage_limit or
                 usage_count_check.valid_to <= timezone.now()):
                usage_count_check.is_active = False
                usage_count_check.save()
        else:
            return redirect('invalid_coupon_code')

        valid_coupon = CouponCode.objects.filter(code=entered_coupon, is_active=True).first()
        
        if valid_coupon:
            course_purchased_form = CoursesPurchasedForm({
                'user'              : current_user,
                'language'          : selected_course.language,
                'course_category'   : selected_course.category,
                'course'            : selected_course
            })
            if course_purchased_form.is_valid():
                course_purchased_form.save()
                course_purchased_form.send_email()
                valid_coupon.usage_count +=1
                valid_coupon.save()
                
            
            return redirect('user_my_learnings')

        else:
            return redirect('invalid_coupon_code')  

    context = {
        'selected_course': selected_course
    }
    return render(request, 'Users/Purchase_Course.html', context)


# User My Learnings
@login_required(login_url='/error_404/')
def user_my_learnings(request):
    current_user = request.user
    user_purchased_courses = CoursesPurchased.objects.filter(user = current_user)

    context = {
        'user_purchased_courses' : user_purchased_courses
    }
    return render(request, 'Users/My_Learnings.html', context)


