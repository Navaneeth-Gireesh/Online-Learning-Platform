from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . models import  CouponCode
import random
from django.utils import timezone
from datetime import timedelta
from . AdminForms import CouponCodeForm
from django.contrib.auth.models import User
from purchases_app.models import CoursesPurchased

# --------------------------- Admin Course Purchase ---------------------------

# Admin Coupons View
@login_required(login_url='/error_404/')
def admin_coupons_view(request):
    if not request.user.is_superuser:
        return redirect('error_404')
    
    all_coupons = CouponCode.objects.all()
    coupon_count = all_coupons.count()
    active_coupons = all_coupons.filter(is_active = True).count()

    context = {
        'all_coupons'   : all_coupons,
        'coupon_count'  : coupon_count,
        'active_coupons' : active_coupons,
    }

    return render(request, 'Admins/Coupons_View.html', context)

# Admin Coupon Create
@login_required(login_url='/error_404/')
def admin_coupon_create(request):
    if not request.user.is_superuser:
        return redirect('error_404')
    
    # Random Coupon Code Generator
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    uppercase_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    random_list = []
    for i in range(3):
        random_list.append(random.choice(numbers))
    for i in range(3):
        random_list.append(random.choice(uppercase_alphabets))
    for i in range(3):
        random_list.append(random.choice(lowercase_alphabets))

    random.shuffle(random_list)

    random_code = ''
    for code in random_list:
        random_code += str(code)

    CouponCode.objects.create(
        code = random_code,
        is_active = True,
        valid_from = timezone.now(),
        valid_to = timezone.now() + timedelta(days = 5),
        usage_count = 0,
        usage_limit = 5 

    )
    return redirect('admin_coupons_view')


# Admin Coupon Edit
@login_required(login_url='/error_404/')
def admin_coupon_edit(request, coupon_id):
    if not request.user.is_superuser:
        return redirect('error_404')
    
    selected_coupon_code = CouponCode.objects.get(id = coupon_id)

    if request.method == 'POST':
        coupon_code_form = CouponCodeForm(request.POST, instance = selected_coupon_code)
        if coupon_code_form.is_valid():
            coupon_code_form.save()
            return redirect('admin_coupons_view')
        else:
            return redirect('index')
    else:
        coupon_code_form = CouponCodeForm(instance = selected_coupon_code)
    
    context = {
        'coupon_code_form' : coupon_code_form
    }
    
    return render(request, 'Admins/Coupon_Edit.html',context)


# Admin Coupon Delete
@login_required(login_url='/error_404/')
def admin_coupon_delete(request, coupon_id):
    if not request.user.is_superuser:
        return redirect('error_404')
    
    coupon_code = CouponCode.objects.filter(id = coupon_id)
    coupon_code.delete()
    return redirect('admin_coupons_view')



# Admin User Enrolled Courses View
@login_required(login_url='/error_404/')
def admin_user_enrolled_courses_view(request, user_id):
    if not request.user.is_superuser:
        return redirect('error_404')
    selected_user = User.objects.get(id = user_id)
    enrolled_courses = CoursesPurchased.objects.filter(user = selected_user)

    context = {
        'selected_user'      : selected_user,
        'enrolled_courses'   : enrolled_courses,
    }
    
    return render(request, 'Admins/Users/Courses/All_Enrolled_Courses.html', context)