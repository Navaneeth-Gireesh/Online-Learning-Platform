from typing import Any
from django.db import models
from courses_app.models import Language, Course_Category, Course, Section, Sub_Section
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

# Quiz Model
class Quiz(models.Model):
    language            = models.ForeignKey(Language, on_delete=models.CASCADE, help_text="Select the Language of the Quiz")
    course_category     = models.ForeignKey(Course_Category, on_delete=models.CASCADE, help_text="Select the Category of the Quiz")
    course              = models.ForeignKey(Course, on_delete=models.CASCADE, help_text="Select the Course for the Quiz")
    section             = models.ForeignKey(Section, on_delete=models.CASCADE, help_text="Select the Section of the Quiz")
    sub_section         = models.ForeignKey(Sub_Section, on_delete=models.CASCADE, help_text="Select the Sub Section of the Quiz")
    title               = models.CharField(max_length=250, help_text="Give a Title for the Quiz")
    slug                = models.SlugField(max_length=255,unique=True, blank=True, null=True)
    order               = models.PositiveIntegerField()

    class Meta:
        verbose_name            = 'Quiz'
        verbose_name_plural     = 'Quizzes'
        unique_together         = ('sub_section', 'order')
        ordering                = ['sub_section', 'order']

    
    def save(self, *args, **kwargs):
        if not self.slug or not self.pk:
            self.slug                       = slugify(f'{self.language}-{self.course_category}-{self.course}-{self.section}-{self.sub_section}-{self.title}')
        else:
            current_quiz                    = Quiz.objects.filter(pk=self.pk).first()
            if current_quiz:
                if (self.language           != current_quiz.language or
                    self.course_category    != current_quiz.course_category or
                    self.course             != current_quiz.course or
                    self.section            != current_quiz.section or
                    self.sub_section        != current_quiz.sub_section or
                    self.title              != current_quiz.title):
                    
                    self.slug               = slugify(f'{self.language}-{self.course_category}-{self.course}-{self.section}-{self.sub_section}-{self.title}')
        if not self.slug:
            self.slug                       = slugify(f'{self.language}-{self.course_category}-{self.course}-{self.section}-{self.sub_section}-{self.title}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

# Question Model
class Question(models.Model):
    language            = models.ForeignKey(Language, on_delete=models.CASCADE, help_text="Select a Language")
    course_category     = models.ForeignKey(Course_Category, on_delete=models.CASCADE, help_text="Select a Category")
    course              = models.ForeignKey(Course, on_delete=models.CASCADE, help_text="Select a Course")
    section             = models.ForeignKey(Section, on_delete=models.CASCADE, help_text="Select a Section")
    sub_section         = models.ForeignKey(Sub_Section, on_delete=models.CASCADE, help_text="Select a Sub Section")
    quiz                = models.ForeignKey(Quiz, on_delete=models.CASCADE, help_text="Select a Quiz")
    question            = models.TextField(help_text="Enter a Question")
    slug                = models.SlugField(max_length=255,unique=True, blank=True, null=True)
    order               = models.PositiveIntegerField()

    class Meta:
        verbose_name            = 'Question'
        verbose_name_plural     = 'Questions'
        unique_together         = ('quiz', 'order')
        ordering                = ['quiz', 'order']


    def save(self, *args, **kwargs):
        if not self.slug or not self.pk:
            self.slug                       = slugify(f'{self.language}-{self.course_category}-{self.course}-{self.section}-{self.sub_section}-{self.quiz}-{self.question}')
        else:
            current_question                = Question.objects.filter(pk=self.pk).first()
            if current_question:
                if (self.language           != current_question.language or
                    self.course_category    != current_question.course_category or
                    self.course             != current_question.course or
                    self.section            != current_question.section or
                    self.sub_section        != current_question.sub_section or
                    self.quiz               != current_question.quiz or
                    self.question           != current_question.question):
                    
                    self.slug               = slugify(f'{self.language}-{self.course_category}-{self.course}-{self.section}-{self.sub_section}-{self.quiz}-{self.question}')
        if not self.slug:
            self.slug                       = slugify(f'{self.language}-{self.course_category}-{self.course}-{self.section}-{self.sub_section}-{self.quiz}-{self.question}')  

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question


# Answers Model
class Answers(models.Model):
    language            = models.ForeignKey(Language, on_delete=models.CASCADE, help_text="Select aLanguage")
    course_category     = models.ForeignKey(Course_Category, on_delete=models.CASCADE, help_text="Select a Category")
    course              = models.ForeignKey(Course, on_delete=models.CASCADE, help_text="Select a Course")
    section             = models.ForeignKey(Section, on_delete=models.CASCADE, help_text="Select a Section")
    sub_section         = models.ForeignKey(Sub_Section, on_delete=models.CASCADE, help_text="Select a Sub Section")
    quiz                = models.ForeignKey(Quiz, on_delete=models.CASCADE, help_text="Select a Quiz")
    question            = models.ForeignKey(Question, on_delete=models.CASCADE, help_text="Select a Question")
    answer              = models.TextField(help_text="Give an Answer to the Question")
    slug                = models.SlugField(max_length=255,unique=True, blank=True, null=True)
    order               = models.PositiveIntegerField()
    is_correct          = models.BooleanField(default=False, help_text='1-Means Correct Answer')

    class Meta:
        verbose_name            = 'Answer'
        verbose_name_plural     = 'Answers'
        unique_together         = ('question', 'order')
        ordering                = ['question', 'order']

    def save(self, *args, **kwargs):
        if not self.slug or not self.pk:
            self.slug                       = slugify(f'{self.language}-{self.course_category}-{self.course}-{self.section}-{self.sub_section}-{self.quiz}-{self.question}-{self.order}')
        else:
            current_answer                  = Answers.objects.filter(pk=self.pk).first()
            if current_answer:
                if (self.language           != current_answer.language or
                    self.course_category    != current_answer.course_category or
                    self.course             != current_answer.course or
                    self.section            != current_answer.section or
                    self.sub_section        != current_answer.sub_section or
                    self.quiz               != current_answer.quiz or
                    self.question           != current_answer.question or
                    self.order              != current_answer.order):
                    
                    self.slug               = slugify(f'{self.language}-{self.course_category}-{self.course}-{self.section}-{self.sub_section}-{self.quiz}-{self.question}-{self.order}')
        if not self.slug:
            self.slug                       = slugify(f'{self.language}-{self.course_category}-{self.course}-{self.section}-{self.sub_section}-{self.quiz}-{self.question}-{self.order}')  

        super().save(*args, **kwargs)

    def __str__(self):
        return self.answer




# User Marks

class UserMarks(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    language            = models.ForeignKey(Language, on_delete=models.CASCADE)
    course_category     = models.ForeignKey(Course_Category, on_delete=models.CASCADE)
    course              = models.ForeignKey(Course, on_delete=models.CASCADE)
    section             = models.ForeignKey(Section, on_delete=models.CASCADE)
    sub_section         = models.ForeignKey(Sub_Section, on_delete=models.CASCADE)
    quiz                = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    marks               = models.PositiveIntegerField()
    slug                = models.SlugField(max_length=255,unique=True, blank=True, null=True)

    class Meta:
        verbose_name        = 'User Marks'
        verbose_name_plural = 'User Marks'

    def save(self, *args, **kwargs):
        if not self.slug or self.pk:
            self.slug               = slugify(f'{self.user.username}-{self.language}-{self.course_category}-{self.course}-{self.section}-{self.sub_section}-{self.quiz}')
        else:
            current_user_marks               = UserMarks.objects.filter(pk=self.pk).first()
            if current_user_marks:
                if (self.user.username      != current_user_marks.user.username or
                    self.language           != current_user_marks.language or
                    self.course_category    != current_user_marks.course_category or
                    self.course             != current_user_marks.course or
                    self.section            != current_user_marks.section or
                    self.sub_section        != current_user_marks.sub_section or
                    self.quiz               != current_user_marks.quiz):
                    
                    self.slug       = slugify(f'{self.user.username}-{self.language}-{self.course_category}-{self.course}-{self.section}-{self.sub_section}-{self.quiz}')
        if not self.slug:
            self.slug               = slugify(f'{self.user.username}-{self.language}-{self.course_category}-{self.course}-{self.section}-{self.sub_section}-{self.quiz}')  

        super().save(*args, **kwargs)

