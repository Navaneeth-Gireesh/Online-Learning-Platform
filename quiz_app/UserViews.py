from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Quiz, Question, Answers, User, UserMarks
from courses_app.models import Sub_Section
from django.urls import reverse

# Create your views here.

# ------------------------------------- User Quiz ------------------------------------------


# User Quiz Home View
@login_required(login_url='/error_404/')
def user_quiz_home_view(request, quiz_slug):
    quiz_selected       = get_object_or_404(Quiz, slug = quiz_slug)
    questions           = Question.objects.filter(quiz=quiz_selected).order_by('-order') 
    question_order      = questions.first()
    user_marks          = UserMarks.objects.filter(quiz = quiz_selected, user = request.user).first()   

    result = False
    if user_marks and question_order:
        if user_marks.marks > question_order.order/2:
            result = True

    context = {
        'quiz_selected' : quiz_selected,
        'questions'     : questions,
        'question_order': question_order,
        'user_marks'    : user_marks,
        'result'        : result,
    }
    return render(request, 'Users/Quiz/Quiz_Home.html', context)


# User Quiz Exam
@login_required(login_url='/error_404/')
def user_quiz_exam(request, quiz_slug):
    selected_quiz = get_object_or_404(Quiz, slug=quiz_slug)
    quiz_questions = Question.objects.filter(quiz=selected_quiz).order_by('order')
    question_answers = Answers.objects.filter(question__in=quiz_questions)
    user_marks = UserMarks.objects.filter(quiz=selected_quiz, user=request.user).first()

    total_score = 0  

    if request.method == 'POST':
        submitted_quiz = request.POST
        
        for question in quiz_questions:
            selected_answer_id = submitted_quiz.get(f'question_{question.id}')
            if selected_answer_id:
                selected_answer = Answers.objects.get(id=selected_answer_id)
                if selected_answer.is_correct:
                    total_score += 1

        if user_marks:
            last_score = user_marks.marks
            if total_score > last_score:
                user_marks.marks = total_score
                user_marks.save()
        else:
            UserMarks.objects.create(
                user=request.user,
                language=selected_quiz.language,
                course_category=selected_quiz.course_category,
                course=selected_quiz.course,
                section=selected_quiz.section,
                sub_section=selected_quiz.sub_section,
                quiz=selected_quiz,
                marks=total_score
            )
        return redirect(reverse('user_quiz_home_view', kwargs={'quiz_slug' : quiz_slug}))

    context = {
        'selected_quiz': selected_quiz,
        'quiz_questions': quiz_questions,
        'question_answers': question_answers
    }
    return render(request, 'Users/Quiz/Quiz_Exam.html', context)