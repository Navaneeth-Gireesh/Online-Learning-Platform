from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .AdminForms import CourseLanguageCreateForm, CourseCategoryCreateForm, CourseCreateForm, CourseInfoCreateForm, CourseTrailerCreateForm
from .AdminForms import CourseSectionCreateForm, CourseSubSectionCreateForm, CourseVideoCreateForm, CourseDocumentCreateForm
from .models import Language, Course_Category, Course, Course_Info, Course_Trailer, Section, Sub_Section, Video, Document
from django.urls import reverse

# Create your views here.


# --------------------------- Admin Course Language View ---------------------------

# Admin Course Languages Create
@login_required(login_url='/error_404/')
def admin_course_languages_create(request):
    if not request.user.is_superuser:
        return redirect('base')
    if request.method == 'POST':
        language_create_form = CourseLanguageCreateForm(request.POST)
        if language_create_form.is_valid():
            language_create_form.save()
            return redirect('all_languages')
    else:
        language_create_form = CourseLanguageCreateForm()
    return render(request, 'Admins/Course_Languages/Course_Languages_Create.html', {'language_create_form' : language_create_form})


# Admin Course Language Edit
@login_required(login_url='/error_404/')
def admin_course_language_edit(request,language_slug):
    if not request.user.is_superuser:
        return redirect('base')
    
    try:
        language_selected = Language.objects.get(slug = language_slug)
    except Language.DoesNotExist:
        return redirect('all_languages')
    
    if request.method == 'POST':
        language_edit_form = CourseLanguageCreateForm(request.POST, instance=language_selected)
        if language_edit_form.is_valid():
            language_edit_form.save()
            return redirect('all_languages')
    else:
        language_edit_form = CourseLanguageCreateForm(instance=language_selected)

    context = {
        'language_edit_form': language_edit_form,
        'language_selected': language_selected
    }
    return render(request, 'Admins/Course_Languages/Course_Language_Edit.html', context)

# Admin Course Language Delete
@login_required(login_url='/error_404/')
def admin_course_language_delete(request, language_slug):
    if not request.user.is_superuser:
        return redirect('error_404')
    
    language_selected = get_object_or_404(Language, slug=language_slug)
    language_selected.delete()
    return redirect('all_languages')




# ------------------------------ Admin Course Categories ----------------------------------


# Admin Course Category View 
@login_required(login_url='/error_404/')
def admin_language_course_category_view(request,language_slug):
    if not request.user.is_superuser:
        return redirect('base')
    
    try:
        language_selected = Language.objects.get(slug = language_slug)
    except Language.DoesNotExist:
        return redirect('base')
    
    course_categories = Course_Category.objects.filter(language = language_selected)

    context = {
        'course_categories' : course_categories,
        'language_selected' : language_selected
    }
    
    return render(request, 'Admins/Course_Categories/All_Course_Categories.html', context)


# Admin Course Category Create
@login_required(login_url='/error_404/')
def admin_course_category_create(request, language_slug):
    if not request.user.is_superuser:
        return redirect('error_404')

    language_selected = get_object_or_404(Language, slug=language_slug)

    if request.method == 'POST':
        category_form = CourseCategoryCreateForm(request.POST, initial={'language': language_selected})
        if category_form.is_valid():
            category = category_form.save(commit=False)
            category.language = language_selected  # Set the language explicitly
            category.save()
            return redirect('admin_language_course_category_view', language_slug=language_slug)
    else:
        category_form = CourseCategoryCreateForm(initial={'language': language_selected})

    context = {
        'category_form': category_form,
        'language_selected': language_selected,
    }
    return render(request, 'Admins/Course_Categories/Course_Category_Create.html', context)


# Admin Course Category Edit
@login_required(login_url='/error_404/')
def admin_course_category_edit(request, category_slug):
    if not request.user.is_superuser:
        return redirect('base')
    
    try:
        category_selected = Course_Category.objects.get(slug=category_slug)
    except Course_Category.DoesNotExist:
        return redirect('all_languages')
    
    if request.method == 'POST':
        course_category_edit_form = CourseCategoryCreateForm(request.POST, instance=category_selected)
        if course_category_edit_form.is_valid():
            course_category_edit_form.save()
            return redirect(reverse('admin_language_course_category_view', kwargs={'language_slug': category_selected.language.slug}))
    else:
        course_category_edit_form = CourseCategoryCreateForm(instance=category_selected)
    
    context = {
        'course_category_edit_form': course_category_edit_form,
        'category_selected': category_selected
    }
    return render(request, 'Admins/Course_Categories/Course_Category_Edit.html', context)

# Admin Course Category Delete
@login_required(login_url='/error_404/')
def admin_course_category_delete(request, category_slug):
    if not request.user.is_superuser:
        return redirect('error_404')
    
    category_selected = get_object_or_404(Course_Category, slug=category_slug)
    category_selected.delete()
    return redirect(reverse('admin_language_course_category_view', kwargs={'language_slug': category_selected.language.slug}))




# ------------------------------------- Admin Courses------------------------------------------

# Admin Course  View 
@login_required(login_url='/error_404/')
def admin_course_view(request,category_slug):
    if not request.user.is_superuser:
        return redirect('base')
    
    try:
        category_selected = Course_Category.objects.get(slug = category_slug)
        language_selected = Language.objects.get(language = category_selected.language)
    except Course_Category.DoesNotExist:
        return redirect('base')
    
    courses = Course.objects.filter(category = category_selected)

    context = {
        'courses' : courses,
        'language_selected' : language_selected,
        'category_selected' : category_selected
    }
    
    return render(request, 'Admins/Courses/All_Courses.html', context)


# Admin Course  Create
@login_required(login_url='/error_404/')
def admin_course_create(request, category_slug):
    if not request.user.is_superuser:
        return redirect('error_404')

    category_selected = get_object_or_404(Course_Category, slug=category_slug)

    if request.method == 'POST':
        course_create_form = CourseCreateForm(request.POST)
        if course_create_form.is_valid():
            course = course_create_form.save(commit=False)
            course.language = category_selected.language  
            course.category = category_selected
            course.save()

            course_create_form.save_m2m() # Many to Many Field Saving
            return redirect('admin_course_view', category_slug=category_slug)
    else:
        course_create_form = CourseCreateForm(initial={'language': category_selected.language, 'category' : category_selected})

    context = {
        'course_create_form' : course_create_form
    }
    return render(request, 'Admins/Courses/Course_Create.html', context)


# Admin Course Edit
@login_required(login_url='/error_404/')
def admin_course_edit(request, course_slug):
    if not request.user.is_superuser:
        return redirect('base')
    
    try:
        course_selected = Course.objects.get(slug=course_slug)
    except Course.DoesNotExist:
        return redirect('admin_course_view')
    
    if request.method == 'POST':
        course_edit_form = CourseCreateForm(request.POST, instance=course_selected)
        if course_edit_form.is_valid():
            course_edit_form.save()
            return redirect(reverse('admin_course_view', kwargs={'category_slug': course_selected.category.slug}))
    else:
        course_edit_form = CourseCreateForm(instance=course_selected)
    
    context = {
        'course_edit_form': course_edit_form,
        'course_selected': course_selected
    }
    return render(request, 'Admins/Courses/Course_Edit.html', context)

# Admin Course Delete
@login_required(login_url='/error_404/')
def admin_course_delete(request, course_slug):
    if not request.user.is_superuser:
        return redirect('error_404')
    
    course_selected = get_object_or_404(Course, slug=course_slug)
    course_selected.delete()
    return redirect(reverse('admin_course_view', kwargs={'category_slug': course_selected.category.slug}))




# ------------------------------------- Admin Course Info------------------------------------------


# Admin Course  View 
@login_required(login_url='/error_404/')
def admin_course_info(request, course_slug):
    if not request.user.is_superuser:
        return redirect('base')
    
    try:
        course_selected = Course.objects.get(slug = course_slug)
    except Course.DoesNotExist:
        return redirect('base')
    
    course_info = Course_Info.objects.filter(course = course_selected)

    context = {
        'course_info' : course_info,
        'course_selected' : course_selected
    }
    
    return render(request, 'Admins/Course_Info/All_Course_Info.html', context)


# Admin Course  Create
@login_required(login_url='/error_404/')
def admin_course_info_create(request, course_slug):
    if not request.user.is_superuser:
        return redirect('error_404')

    course_selected = get_object_or_404(Course, slug = course_slug)

    if request.method == 'POST':
        course_info_form = CourseInfoCreateForm(request.POST)
        if course_info_form.is_valid():
            course_info = course_info_form.save(commit=False)
            course_info.language = course_selected.language
            course_info.category = course_selected.category
            course_info.course   = course_selected
            course_info.save()
            return redirect('admin_course_info', course_slug=course_slug)
    else:
        course_info_form = CourseInfoCreateForm(initial={'language': course_selected.language, 'category' : course_selected.category, 'course': course_selected})

    context = {
        'course_info_form' : course_info_form
    }
    return render(request, 'Admins/Course_Info/Course_Info_Create.html', context)


# Admin Course Edit
@login_required(login_url='/error_404/')
def admin_course_info_edit(request, course_info_slug):
    if not request.user.is_superuser:
        return redirect('base')
    
    try:
        course_info_selected = Course_Info.objects.get(slug=course_info_slug)
    except Course_Info.DoesNotExist:
        return redirect('admin_course_info')
    
    if request.method == 'POST':
        course_info_edit_form = CourseInfoCreateForm(request.POST, instance=course_info_selected)
        if course_info_edit_form.is_valid():
            course_info_edit_form.save()
            return redirect(reverse('admin_course_info', kwargs={'course_slug': course_info_selected.course.slug}))
    else:
        course_info_edit_form = CourseInfoCreateForm(instance=course_info_selected)
    
    context = {
        'course_info_edit_form': course_info_edit_form,
        'course_info_selected': course_info_selected
    }
    return render(request, 'Admins/Course_Info/Course_Info_Edit.html', context)

# Admin Course Delete
@login_required(login_url='/error_404/')
def admin_course_info_delete(request, course_info_slug):
    if not request.user.is_superuser:
        return redirect('error_404')
    
    course_info_selected = get_object_or_404(Course_Info, slug=course_info_slug)
    course_info_selected.delete()
    return redirect(reverse('admin_course_info', kwargs={'course_slug': course_info_selected.course.slug}))


# ------------------------------------- Admin Course Trailer ------------------------------------------

# Admin Course Trailer View
@login_required(login_url='/error_404/')
def admin_course_trailer_view(request, course_slug):
    if not request.user.is_superuser:
        return redirect('base')
    
    try:
        course_selected = Course.objects.get(slug = course_slug)
    except Course.DoesNotExist:
        return redirect('base')
    
    course_trailers = Course_Trailer.objects.filter(course = course_selected)

    context = {
        'course_trailers' : course_trailers,
        'course_selected' : course_selected
    }
    
    return render(request, 'Admins/Course_Trailers/All_Trailers.html', context)

# Admin Course Trailer  Create
@login_required(login_url='/error_404/')
def admin_course_trailer_create(request, course_slug):
    if not request.user.is_superuser:
        return redirect('error_404')

    course_selected = get_object_or_404(Course, slug = course_slug)

    if request.method == 'POST':
        course_trailer_form = CourseTrailerCreateForm(request.POST)
        if course_trailer_form.is_valid():
            course_trailer = course_trailer_form.save(commit=False)
            course_trailer.language = course_selected.language
            course_trailer.category = course_selected.category
            course_trailer.course   = course_selected
            course_trailer.save()
            return redirect('admin_course_trailer_view', course_slug=course_slug)
    else:
        course_trailer_form = CourseTrailerCreateForm(initial={'language': course_selected.language, 'category' : course_selected.category, 'course': course_selected})

    context = {
        'course_trailer_form' : course_trailer_form
    }
    return render(request, 'Admins/Course_Trailers/Course_Trailer_Create.html', context)

# Admin Course Trailer Edit
@login_required(login_url='/error_404/')
def admin_course_trailer_edit(request, course_trailer_slug):
    if not request.user.is_superuser:
        return redirect('base')
    
    try:
        course_trailer_selected = Course_Trailer.objects.get(slug=course_trailer_slug)
    except Course_Trailer.DoesNotExist:
        return redirect('admin_course_view')
    
    if request.method == 'POST':
        course_trailer_edit_form = CourseTrailerCreateForm(request.POST, instance=course_trailer_selected)
        if course_trailer_edit_form.is_valid():
            course_trailer_edit_form.save()
            return redirect(reverse('admin_course_trailer_view', kwargs={'course_slug': course_trailer_selected.course.slug}))
    else:
        course_trailer_edit_form = CourseTrailerCreateForm(instance=course_trailer_selected)
    
    context = {
        'course_trailer_edit_form': course_trailer_edit_form,
        'course_trailer_selected': course_trailer_selected
    }
    return render(request, 'Admins/Course_Trailers/Course_Trailer_Edit.html', context)


# Admin Course Trailer Delete
@login_required(login_url='/error_404/')
def admin_course_trailer_delete(request, course_trailer_slug):
    if not request.user.is_superuser:
        return redirect('error_404')
    
    course_trailer_selected = get_object_or_404(Course_Trailer, slug=course_trailer_slug)
    course_trailer_selected.delete()
    return redirect(reverse('admin_course_trailer_view', kwargs={'course_slug': course_trailer_selected.course.slug}))


# ------------------------------------- Admin Course section ------------------------------------------

# Admin Course Section View
@login_required(login_url='/error_404/')
def admin_course_section_view(request, course_slug):
    if not request.user.is_superuser:
        return redirect('base')
    
    try:
        course_selected = Course.objects.get(slug = course_slug)
    except Course.DoesNotExist:
        return redirect('base')
    
    course_sections = Section.objects.filter(course = course_selected)

    context = {
        'course_sections' : course_sections,
        'course_selected' : course_selected
    }
    
    return render(request, 'Admins/Sections/All_Sections.html', context)


# Admin Course Section  Create
@login_required(login_url='/error_404/')
def admin_course_section_create(request, course_slug):
    if not request.user.is_superuser:
        return redirect('error_404')

    course_selected = get_object_or_404(Course, slug = course_slug)

    if request.method == 'POST':
        course_section_form = CourseSectionCreateForm(request.POST)
        if course_section_form.is_valid():
            course_section = course_section_form.save(commit=False)
            course_section.language = course_selected.language
            course_section.category = course_selected.category
            course_section.course   = course_selected
            course_section.save()
            return redirect('admin_course_section_view', course_slug=course_slug)
    else:
        course_section_form =CourseSectionCreateForm(initial={'language': course_selected.language, 'category' : course_selected.category, 'course': course_selected})

    context = {
        'course_section_form' : course_section_form,
        'course_selected'     : course_selected
    }
    return render(request, 'Admins/Sections/Course_Section_Create.html', context)


# Admin Course Section Edit
@login_required(login_url='/error_404/')
def admin_course_section_edit(request, section_slug):
    if not request.user.is_superuser:
        return redirect('base')
    
    try:
        course_section_selected = Section.objects.get(slug=section_slug)
    except Section.DoesNotExist:
        return redirect('admin_course_section_view')
    
    if request.method == 'POST':
        course_section_edit_form = CourseSectionCreateForm(request.POST, instance=course_section_selected)
        if course_section_edit_form.is_valid():
            course_section_edit_form.save()
            return redirect(reverse('admin_course_section_view', kwargs={'course_slug': course_section_selected.course.slug}))
    else:
        course_section_edit_form = CourseSectionCreateForm(instance=course_section_selected)
    
    context = {
        'course_section_edit_form': course_section_edit_form,
        'course_section_selected': course_section_selected
    }
    return render(request, 'Admins/Sections/Course_Section_Edit.html', context)


# Admin Course Section Delete
@login_required(login_url='/error_404/')
def admin_course_section_delete(request, section_slug):
    if not request.user.is_superuser:
        return redirect('error_404')
    
    course_section_selected = get_object_or_404(Section, slug=section_slug)
    course_section_selected.delete()
    return redirect(reverse('admin_course_section_view', kwargs={'course_slug': course_section_selected.course.slug}))


# ------------------------------------- Admin Course Sub Section ------------------------------------------

# Admin Course Sub Section View
@login_required(login_url='/error_404/')
def admin_course_sub_section_view(request, section_slug):
    if not request.user.is_superuser:
        return redirect('base')
    
    try:
        section_selected = Section.objects.get(slug = section_slug)
    except Section.DoesNotExist:
        return redirect('base')
    
    sub_section_selected = Sub_Section.objects.filter(section = section_selected)

    context = {
        'section_selected' : section_selected,
        'sub_section_selected' : sub_section_selected
    }
    
    return render(request, 'Admins/Sub_Sections/All_Sub_Sections.html', context)


# Admin Course Sub Section  Create
@login_required(login_url='/error_404/')
def admin_course_sub_section_create(request, section_slug):
    if not request.user.is_superuser:
        return redirect('error_404')

    section_selected = get_object_or_404(Section, slug = section_slug)

    if request.method == 'POST':
        course_sub_section_form = CourseSubSectionCreateForm(request.POST)
        if course_sub_section_form.is_valid():
            course_sub_section = course_sub_section_form.save(commit=False)
            course_sub_section.language = section_selected.language
            course_sub_section.category = section_selected.category
            course_sub_section.course   = section_selected.course
            course_sub_section.section  = section_selected
            course_sub_section.save()
            return redirect('admin_course_sub_section_view', section_slug=section_slug)
    else:
        course_sub_section_form =CourseSubSectionCreateForm(initial={'language': section_selected.language, 'category' : section_selected.category, 'course': section_selected.course, 'section': section_selected})

    context = {
        'course_sub_section_form' : course_sub_section_form,
        'section_selected'     : section_selected
    }
    return render(request, 'Admins/Sub_Sections/Course_Sub_Section_Create.html', context)


# Admin Course Sub Section Edit
@login_required(login_url='/error_404/')
def admin_course_sub_section_edit(request, sub_section_slug):
    if not request.user.is_superuser:
        return redirect('base')
    
    try:
        course_sub_section_selected = Sub_Section.objects.get(slug=sub_section_slug)
    except Sub_Section.DoesNotExist:
        return redirect('admin_course_sub_section_view')
    
    if request.method == 'POST':
        course_sub_section_edit_form = CourseSubSectionCreateForm(request.POST, instance=course_sub_section_selected)
        if course_sub_section_edit_form.is_valid():
            course_sub_section_edit_form.save()
            return redirect(reverse('admin_course_sub_section_view', kwargs={'section_slug': course_sub_section_selected.section.slug}))
    else:
        course_sub_section_edit_form = CourseSubSectionCreateForm(instance=course_sub_section_selected)
    
    context = {
        'course_sub_section_edit_form': course_sub_section_edit_form,
        'course_sub_section_selected': course_sub_section_selected
    }
    return render(request, 'Admins/Sub_Sections/Course_Sub_Section_Edit.html', context)


# Admin Course Sub Section Delete
@login_required(login_url='/error_404/')
def admin_course_sub_section_delete(request, sub_section_slug):
    if not request.user.is_superuser:
        return redirect('error_404')
    
    course_sub_section_selected = get_object_or_404(Sub_Section, slug=sub_section_slug)
    course_sub_section_selected.delete()
    return redirect(reverse('admin_course_sub_section_view', kwargs={'section_slug': course_sub_section_selected.section.slug}))



# ------------------------------------- Admin Course Video ------------------------------------------

# Admin Course Video View
@login_required(login_url='/error_404/')
def admin_course_video_view(request, sub_section_slug):
    if not request.user.is_superuser:
        return redirect('base')
    
    try:
        sub_section_selected = Sub_Section.objects.get(slug = sub_section_slug)
    except Sub_Section.DoesNotExist:
        return redirect('base')
    
    videos_selected = Video.objects.filter(sub_section = sub_section_selected)

    context = {
        'sub_section_selected' : sub_section_selected,
        'videos_selected' : videos_selected
    }
    
    return render(request, 'Admins/Videos/All_videos.html', context)


# Admin Course Video Create
@login_required(login_url='/error_404/')
def admin_course_video_create(request, sub_section_slug):
    if not request.user.is_superuser:
        return redirect('error_404')

    sub_section_selected = get_object_or_404(Sub_Section, slug = sub_section_slug)

    if request.method == 'POST':
        course_video_form = CourseVideoCreateForm(request.POST)
        if course_video_form.is_valid():
            course_video = course_video_form.save(commit=False)
            course_video.language       = sub_section_selected.language
            course_video.category       = sub_section_selected.category
            course_video.course         = sub_section_selected.course
            course_video.section        = sub_section_selected.section
            course_video.sub_section    = sub_section_selected
            course_video.save()
            return redirect('admin_course_video_view', sub_section_slug=sub_section_slug)
    else:
        course_video_form =CourseVideoCreateForm(initial={'language': sub_section_selected.language, 'category' : sub_section_selected.category, 'course': sub_section_selected.course, 'section': sub_section_selected.section, 'sub_section' : sub_section_selected})

    context = {
        'course_video_form' : course_video_form,
        'sub_section_selected'     : sub_section_selected
    }
    return render(request, 'Admins/Videos/Video_Create.html', context)


# Admin Course Video Edit
@login_required(login_url='/error_404/')
def admin_course_video_edit(request, video_slug):
    if not request.user.is_superuser:
        return redirect('base')

    video_selected = get_object_or_404(Video, slug=video_slug)

    if request.method == 'POST':
        video_edit_form = CourseVideoCreateForm(request.POST, instance=video_selected)
        if video_edit_form.is_valid():
            video_edit_form.save()
            return redirect(reverse('admin_course_video_view', kwargs={'sub_section_slug': video_selected.sub_section.slug}))
    else:
        video_edit_form = CourseVideoCreateForm(instance=video_selected)
    
    context = {
        'video_edit_form': video_edit_form,
        'video_selected': video_selected
    }
    return render(request, 'Admins/Videos/Video_Edit.html', context)


# Admin Course Video Delete
@login_required(login_url='/error_404/')
def admin_course_video_delete(request, video_slug):
    if not request.user.is_superuser:
        return redirect('error_404')
    
    video_selected = get_object_or_404(Video, slug=video_slug)
    video_selected.delete()
    return redirect(reverse('admin_course_video_view', kwargs={'sub_section_slug': video_selected.sub_section.slug}))



# ------------------------------------- Admin Course Documents ------------------------------------------

# Admin Course Video View
@login_required(login_url='/error_404/')
def admin_video_document_view(request, video_slug):
    if not request.user.is_superuser:
        return redirect('base')
    

    videos_selected  = get_object_or_404(Video, slug = video_slug)

    
    documents_selected = Document.objects.filter(video = videos_selected)

    context = {
        'documents_selected' : documents_selected,
        'videos_selected' : videos_selected
    }
    
    return render(request, 'Admins/Documents/All_Documents.html', context)


# Admin Course Video Create
@login_required(login_url='/error_404/')
def admin_video_document_create(request, video_slug):
    if not request.user.is_superuser:
        return redirect('error_404')

    video_selected = get_object_or_404(Video, slug = video_slug)

    if request.method == 'POST':
        document_form = CourseDocumentCreateForm(request.POST)
        if document_form.is_valid():
            video_document = document_form.save(commit=False)
            video_document.language       = video_document.language
            video_document.category       = video_document.category
            video_document.course         = video_document.course
            video_document.section        = video_document.section
            video_document.sub_section    = video_selected.sub_section
            video_document.video          = video_selected
            video_document.save()
            return redirect('admin_video_document_view', video_slug=video_slug)
    else:
        document_form =CourseDocumentCreateForm(initial={'language': video_selected.language, 'category' : video_selected.category, 'course': video_selected.course, 'section': video_selected.section, 'sub_section' : video_selected.sub_section, 'video': video_selected})

    context = {
        'document_form'         : document_form,
        'video_selected'        : video_selected
    }
    return render(request, 'Admins/Documents/Document_Create.html', context)


# Admin Course Video Edit
@login_required(login_url='/error_404/')
def admin_video_document_edit(request, document_slug):
    if not request.user.is_superuser:
        return redirect('base')

    document_selected = get_object_or_404(Document, slug=document_slug)

    if request.method == 'POST':
        document_edit_form = CourseDocumentCreateForm(request.POST, instance=document_selected)
        if document_edit_form.is_valid():
            document_edit_form.save()
            return redirect(reverse('admin_video_document_view', kwargs={'video_slug': document_selected.video.slug}))
    else:
        document_edit_form = CourseDocumentCreateForm(instance=document_selected)
    
    context = {
        'document_edit_form': document_edit_form,
        'document_selected': document_selected
    }
    return render(request, 'Admins/Documents/Document_Edit.html', context)


# Admin Course Video Delete
@login_required(login_url='/error_404/')
def admin_video_document_delete(request, document_slug):
    if not request.user.is_superuser:
        return redirect('error_404')
    
    document_selected = get_object_or_404(Document, slug=document_slug)
    document_selected.delete()
    return redirect(reverse('admin_video_document_view', kwargs={'video_slug': document_selected.video.slug}))

