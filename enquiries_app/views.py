from django.shortcuts import render,redirect ,get_object_or_404
from courses_app.models import Language, Course_Category, Course
from .forms import ExpertAdviceForm
# Create your views here.

def expert_advice(request):
    all_languages           = Language.objects.all()
    all_course_categories   = Course_Category.objects.all()
    all_courses             = Course.objects.all()
    
    if request.method == 'POST':
        expert_advice_form = ExpertAdviceForm(request.POST)
        if expert_advice_form.is_valid():
            expert_advice_form.send_email()
            return render(request, 'success.html')
    else:
        expert_advice_form = ExpertAdviceForm()

    context = {
        'all_languages'         : all_languages,
        'all_course_categories' : all_course_categories,
        'all_courses'           : all_courses,
        'expert_advice_form'    : expert_advice_form
    }
    return render(request, 'consultation.html', context)

