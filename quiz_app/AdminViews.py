from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Quiz, Question, Answers
from courses_app.models import Sub_Section
from . AdminForms import CourseQuizCreateForm, QuizQuestionCreateForm, QuizAnswersCreateForm
from django.urls import reverse
# Create your views here.


# ------------------------------------- Admin Quiz ------------------------------------------

# Admin Course Video View
@login_required(login_url='/error_404/')
def admin_course_quiz_view(request, sub_section_slug):
    if not request.user.is_superuser:
        return redirect('base')
    

    sub_section_selected  = get_object_or_404(Sub_Section, slug = sub_section_slug)

    
    quiz_selected = Quiz.objects.filter(sub_section = sub_section_selected)

    context = {
        'sub_section_selected' : sub_section_selected,
        'quiz_selected' : quiz_selected
    }
    
    return render(request, 'Admins/Quiz/All_Quiz.html', context)


# Admin Course Video Create
@login_required(login_url='/error_404/')
def admin_course_quiz_create(request, sub_section_slug):
    if not request.user.is_superuser:
        return redirect('error_404')

    sub_section_selected  = get_object_or_404(Sub_Section, slug = sub_section_slug)

    if request.method == 'POST':
        quiz_create_form = CourseQuizCreateForm(request.POST)
        if quiz_create_form.is_valid():
            sub_section_quiz = quiz_create_form.save(commit=False)
            sub_section_quiz.language           = sub_section_selected.language
            sub_section_quiz.course_category    = sub_section_selected.category
            sub_section_quiz.course             = sub_section_selected.course
            sub_section_quiz.section            = sub_section_selected.section
            sub_section_quiz.sub_section        = sub_section_selected
            sub_section_quiz.save()
            return redirect('admin_course_quiz_view', sub_section_slug=sub_section_slug)
    else:
        quiz_create_form = CourseQuizCreateForm(initial={'language': sub_section_selected.language, 'course_category' : sub_section_selected.category, 'course': sub_section_selected.course, 'section': sub_section_selected.section, 'sub_section' : sub_section_selected})

    context = {
        'quiz_create_form'         : quiz_create_form,
        'sub_section_selected'        : sub_section_selected
    }
    return render(request, 'Admins/Quiz/Quiz_Create.html', context)


# Admin Course Video Edit
@login_required(login_url='/error_404/')
def admin_course_quiz_edit(request, quiz_slug):
    if not request.user.is_superuser:
        return redirect('base')

    quiz_selected = get_object_or_404(Quiz, slug=quiz_slug)

    if request.method == 'POST':
        quiz_edit_form = CourseQuizCreateForm(request.POST, instance=quiz_selected)
        if quiz_edit_form.is_valid():
            quiz_edit_form.save()
            return redirect(reverse('admin_course_quiz_view', kwargs={'sub_section_slug': quiz_selected.sub_section.slug}))
    else:
        quiz_edit_form = CourseQuizCreateForm(instance=quiz_selected)
    
    context = {
        'quiz_edit_form': quiz_edit_form,
        'quiz_selected': quiz_selected
    }
    return render(request, 'Admins/Quiz/Quiz_Edit.html', context)


# Admin Course Video Delete
@login_required(login_url='/error_404/')
def admin_course_quiz_delete(request, quiz_slug):
    if not request.user.is_superuser:
        return redirect('error_404')
    quiz_selected = get_object_or_404(Quiz, slug=quiz_slug)
    quiz_selected.delete()
    return redirect(reverse('admin_course_quiz_view', kwargs={'sub_section_slug': quiz_selected.sub_section.slug}))


# ------------------------------------- Admin Quiz Questions ------------------------------------------

# Admin Course Quiz Question View
@login_required(login_url='/error_404/')
def admin_quiz_question_view(request, quiz_slug):
    if not request.user.is_superuser:
        return redirect('base')
    

    quiz_selected  = get_object_or_404(Quiz, slug = quiz_slug)

    
    question_selected = Question.objects.filter(quiz = quiz_selected)

    context = {
        'question_selected' : question_selected,
        'quiz_selected' : quiz_selected
    }
    
    return render(request, 'Admins/Questions/All_Questions.html', context)


# Admin Course Quiz Question Create
@login_required(login_url='/error_404/')
def admin_quiz_question_create(request, quiz_slug):
    if not request.user.is_superuser:
        return redirect('error_404')

    quiz_selected  = get_object_or_404(Quiz, slug = quiz_slug)

    if request.method == 'POST':
        question_create_form = QuizQuestionCreateForm(request.POST)
        if question_create_form.is_valid():
            quiz_question = question_create_form.save(commit=False)
            quiz_question.language           = quiz_selected.language
            quiz_question.course_category    = quiz_selected.course_category
            quiz_question.course             = quiz_selected.course
            quiz_question.section            = quiz_selected.section
            quiz_question.sub_section        = quiz_selected.sub_section
            quiz_question.quiz               = quiz_selected
            quiz_question.save()
            return redirect('admin_quiz_question_view', quiz_slug=quiz_slug)
    else:
        question_create_form = QuizQuestionCreateForm(initial={'language': quiz_selected.language, 'course_category' : quiz_selected.course_category, 'course': quiz_selected.course, 'section': quiz_selected.section, 'sub_section' : quiz_selected.sub_section, 'quiz' : quiz_selected })

    context = {
        'quiz_selected'               : quiz_selected,
        'question_create_form'        : question_create_form
    }
    return render(request, 'Admins/Questions/Question_Create.html', context)


# Admin Course Quiz Question Edit
@login_required(login_url='/error_404/')
def admin_quiz_question_edit(request, question_slug):
    if not request.user.is_superuser:
        return redirect('base')

    question_selected = get_object_or_404(Question, slug=question_slug)

    if request.method == 'POST':
        question_edit_form = QuizQuestionCreateForm(request.POST, instance=question_selected)
        if question_edit_form.is_valid():
            question_edit_form.save()
            return redirect(reverse('admin_quiz_question_view', kwargs={'quiz_slug': question_selected.quiz.slug}))
    else:
        question_edit_form = QuizQuestionCreateForm(instance=question_selected)
    
    context = {
        'question_edit_form': question_edit_form,
        'question_selected': question_selected
    }
    return render(request, 'Admins/Questions/Question_Edit.html', context)


# Admin Course Quiz Question Delete
@login_required(login_url='/error_404/')
def admin_quiz_question_delete(request, question_slug):
    if not request.user.is_superuser:
        return redirect('error_404')
    question_selected = get_object_or_404(Question, slug=question_slug)
    question_selected.delete()
    return redirect(reverse('admin_quiz_question_view', kwargs={'quiz_slug': question_selected.quiz.slug}))


# ------------------------------------- Admin Quiz Answers ------------------------------------------

# Admin Course Quiz Answers View
@login_required(login_url='/error_404/')
def admin_quiz_answers_view(request, question_slug):
    if not request.user.is_superuser:
        return redirect('base')
    

    question_selected  = get_object_or_404(Question, slug = question_slug)

    
    answer_selected = Answers.objects.filter(question = question_selected)

    context = {
        'question_selected' : question_selected,
        'answer_selected' : answer_selected
    }
    
    return render(request, 'Admins/Answers/All_Answers.html', context)


# Admin Course Quiz Answer Create
@login_required(login_url='/error_404/')
def admin_quiz_answers_create(request, question_slug):
    if not request.user.is_superuser:
        return redirect('error_404')

    question_selected  = get_object_or_404(Question, slug = question_slug)

    if request.method == 'POST':
        answer_create_form = QuizAnswersCreateForm(request.POST)
        if answer_create_form.is_valid():
            quiz_answer = answer_create_form.save(commit=False)
            quiz_answer.language           = question_selected.language
            quiz_answer.course_category    = question_selected.course_category
            quiz_answer.course             = question_selected.course
            quiz_answer.section            = question_selected.section
            quiz_answer.sub_section        = question_selected.sub_section
            quiz_answer.quiz               = question_selected.quiz
            quiz_answer.question           = question_selected
            quiz_answer.save()
            return redirect('admin_quiz_answers_view', question_slug=question_slug)
    else:
        answer_create_form = QuizAnswersCreateForm(initial={'language': question_selected.language, 'course_category' : question_selected.course_category, 'course': question_selected.course, 'section': question_selected.section, 'sub_section' : question_selected.sub_section, 'quiz' : question_selected.quiz, 'question' : question_selected })

    context = {
        'question_selected'             : question_selected,
        'answer_create_form'            : answer_create_form
    }
    return render(request, 'Admins/Answers/Answer_Create.html', context)


# Admin Course Quiz Question Edit
@login_required(login_url='/error_404/')
def admin_quiz_answers_edit(request, answer_slug):
    if not request.user.is_superuser:
        return redirect('base')

    answer_selected = get_object_or_404(Answers, slug=answer_slug)

    if request.method == 'POST':
        answer_edit_form = QuizAnswersCreateForm(request.POST, instance=answer_selected)
        if answer_edit_form.is_valid():
            answer_edit_form.save()
            return redirect(reverse('admin_quiz_answers_view', kwargs={'question_slug':answer_selected.question.slug}))
    else:
        answer_edit_form = QuizAnswersCreateForm(instance=answer_selected)
    
    context = {
        'answer_edit_form'  : answer_edit_form,
        'answer_selected'   : answer_selected
    }
    return render(request, 'Admins/Answers/Answer_Edit.html', context)


# Admin Course Quiz Question Delete
@login_required(login_url='/error_404/')
def admin_quiz_answers_delete(request, answer_slug):
    if not request.user.is_superuser:
        return redirect('error_404')
    answer_selected = get_object_or_404(Answers, slug=answer_slug)
    answer_selected.delete()
    return redirect(reverse('admin_quiz_answers_view', kwargs={'question_slug':answer_selected.question.slug}))
