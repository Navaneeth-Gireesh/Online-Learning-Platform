from django.urls import path, include
from . import AdminViews, UserViews

urlpatterns = [
    # ------------------------------------------------ ADMIN URLS ---------------------------------------------
    # ADMIN ---- Quiz
    path('Admin/Courses/Sub-Section/Quiz/View/<slug:sub_section_slug>', AdminViews.admin_course_quiz_view, name = 'admin_course_quiz_view'),
    path('Admin/Courses/Sub-Section/Quiz/Create/<slug:sub_section_slug>', AdminViews.admin_course_quiz_create, name = 'admin_course_quiz_create'),
    path('Admin/Courses/Sub-Section/Quiz/Edit/<slug:quiz_slug>', AdminViews.admin_course_quiz_edit, name = 'admin_course_quiz_edit'),
    path('Admin/Courses/Sub-Section/Quiz/Delete/<slug:quiz_slug>', AdminViews.admin_course_quiz_delete, name = 'admin_course_quiz_delete'),

    # ADMIN ---- Question
    path('Admin/Courses/Quiz/Question/View/<slug:quiz_slug>', AdminViews.admin_quiz_question_view, name = 'admin_quiz_question_view'),
    path('Admin/Courses/Quiz/Question/Create/<slug:quiz_slug>', AdminViews.admin_quiz_question_create, name = 'admin_quiz_question_create'),
    path('Admin/Courses/Quiz/Question/Edit/<slug:question_slug>', AdminViews.admin_quiz_question_edit, name = 'admin_quiz_question_edit'),
    path('Admin/Courses/Quiz/Question/Delete/<slug:question_slug>', AdminViews.admin_quiz_question_delete, name = 'admin_quiz_question_delete'),

    # ADMIN ---- Answer
    path('Admin/Courses/Question/Answers/View/<slug:question_slug>', AdminViews.admin_quiz_answers_view, name = 'admin_quiz_answers_view'),
    path('Admin/Courses/Question/Answers/Create/<slug:question_slug>', AdminViews.admin_quiz_answers_create, name = 'admin_quiz_answers_create'),
    path('Admin/Courses/Question/Answers/Edit/<slug:answer_slug>', AdminViews.admin_quiz_answers_edit, name = 'admin_quiz_answers_edit'),
    path('Admin/Courses/Question/Answers/Delete/<slug:answer_slug>', AdminViews.admin_quiz_answers_delete, name = 'admin_quiz_answers_delete'),


    # ------------------------------------------------ STUDENT URLS ---------------------------------------------
    path('User/Courses/Quiz/Home/<slug:quiz_slug>', UserViews.user_quiz_home_view, name ='user_quiz_home_view'),
    path('User/Courses/Quiz/Exam/<slug:quiz_slug>', UserViews.user_quiz_exam, name = 'user_quiz_exam'),
]