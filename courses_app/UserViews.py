from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Language, Course_Category, Course, Course_Info, Course_Trailer, Section, Sub_Section, Video, Document
from quiz_app. models import Quiz, Question, Answers
from purchases_app.models import CoursesPurchased
# Create your views here.


# --------------------------- User Course Language View ---------------------------

# User Course Language View
@login_required(login_url='/error_404/')
def user_languages_view(request):
    if request.user.is_authenticated:
        user_language = request.user.profile.language
        if user_language is not None:
            language = get_object_or_404(Language, slug=user_language.slug)
            return redirect('user_course_categories_and_courses', language_slug=language.slug)

    all_languages = Language.objects.all()
    return render(request, 'Users/Languages/Languages.html', {'all_languages': all_languages})

# User Course Categories and Courses View
@login_required(login_url='/error_404/')
def user_course_categories_and_courses(request, language_slug):
    current_user        = request.user
    language_selected   = get_object_or_404(Language, slug = language_slug)
    all_categories      = Course_Category.objects.filter(language = language_selected)
    all_courses         = Course.objects.filter(language = language_selected)
    user_purchases      = CoursesPurchased.objects.filter(user = current_user).values_list('course__title', flat=True)

    course_name = request.GET.get('course_name')
    course_data = None  # Default to None if no search query is provided
    if course_name:
        course_data = Course.objects.filter(title__icontains=course_name, language=language_selected)

    context = {
        'language_selected' : language_selected,
        'all_categories'    : all_categories,
        'all_courses'       : all_courses,
        'user_purchases'    : user_purchases,
        'course_data'       : course_data
    }
    return render(request, 'Users/Course_Categories_and_Courses/Course_Categories_and_Courses.html', context)

# User Course Data View
@login_required(login_url='/error_404/')
def course_data(request, course_slug):
    course_selected     = get_object_or_404(Course, slug = course_slug)
    course_information  = Course_Info.objects.filter(course = course_selected)
    course_trailers     = Course_Trailer.objects.filter(course = course_selected)
    course_sections     = Section.objects.filter(course = course_selected)
    course_sub_sections = Sub_Section.objects.filter(course = course_selected)
    course_videos       = Video.objects.filter(course = course_selected)
    course_documents    = Document.objects.filter(course = course_selected)
    course_quiz         = Quiz.objects.filter(course = course_selected)
    current_user        = request.user
    user_purchases      = CoursesPurchased.objects.filter(user = current_user).values_list('course__title', flat=True)


    context = {
        'course_selected'     : course_selected,
        'course_information'  : course_information,
        'course_trailers'     : course_trailers,
        'course_sections'     : course_sections,
        'course_sub_sections' : course_sub_sections,
        'course_videos'       : course_videos,
        'course_documents'    : course_documents,
        'course_quiz'         : course_quiz,
        'user_purchases'      : user_purchases  

    }

    return render(request, 'Users/Course_Data/Course_Data.html', context)
