from django import forms
from . models import Quiz, Question, Answers

# Admin Quiz Create Form
class CourseQuizCreateForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = [
            'language',
            'course_category',
            'course',
            'section',
            'sub_section',
            'title',
            'order'
        ]
        labels = {
            'language' : 'Language',
            'course_category' : 'Course Category',
            'course' : 'Course',
            'section' : 'Section',
            'sub_section' : 'Sub Section',
            'title' : 'Title',
            'order' : 'Order'
        }
# Admin Question Create Form
class QuizQuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'language',
            'course_category',
            'course',
            'section',
            'sub_section',
            'quiz',
            'question',
            'order'
        ]
        labels = {
            'language' : 'Language',
            'course_category' :'Course Category',
            'course' : 'Course',
            'section' : 'Section',
            'sub_section' : 'Sub Section',
            'quiz' : 'Quiz',
            'question' : 'Question',
            'order' : 'Order'
        }

# Admin Answers Create Form
class QuizAnswersCreateForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = [
            'language',
            'course_category',
            'course',
            'section',
            'sub_section',
            'quiz',
            'question',
            'answer',
            'is_correct',
            'order'
        ]
        labels = {
             'language' : 'Language',
            'course_category' :'Course Category',
            'course' : 'Course',
            'section' : 'Section',
            'sub_section' : 'Sub Section',
            'quiz' : 'Quiz',
            'question' : 'Question',
            'answer' : 'Answer',
            'is_correct' : 'Is Correct',
            'order' : 'Order'
        }