from django.contrib import admin
from . models import Quiz, Question, Answers, UserMarks

# Register your models here.

# Quiz Admin
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'language',
                    'course_category',
                    'course',
                    'section',
                    'sub_section'
                    )
    readonly_fields = ('slug',)
    list_filter = ('language',
                    'course_category',
                    'course',
                    'section',
                    'sub_section',
                    )
    search_fields = ('title',
                    'language',
                    'course_category',
                    'course',
                    'section',
                    'sub_section',
                    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related(
            'language', 'course_category', 'course', 'section', 'sub_section', 'quiz'
        )
    
admin.site.register(Quiz, QuizAdmin)

# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question',
                    'language',
                    'course_category',
                    'course',
                    'section',
                    'sub_section',
                    'quiz'
                    )
    readonly_fields = ('slug',)
    list_filter = ('language',
                    'course_category',
                    'course',
                    'section',
                    'sub_section',
                    'quiz',
                    )
    search_fields = ('question',
                    'language',
                    'course_category',
                    'course',
                    'section',
                    'sub_section',
                    'quiz',
                    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related(
            'language', 'course_category', 'course', 'section', 'sub_section', 'quiz'
        )
    
admin.site.register(Question, QuestionAdmin)


# Answer Admin
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer',
                    'question',
                    'language',
                    'course_category',
                    'course',
                    'section',
                    'sub_section',
                    'quiz'
                    )
    readonly_fields = ('slug',)
    list_filter = ( 'question',
                    'language',
                    'course_category',
                    'course',
                    'section',
                    'sub_section',
                    'quiz',
                    )
    search_fields = ('question',
                    'language',
                    'course_category',
                    'course',
                    'section',
                    'sub_section',
                    'quiz',
                    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related(
            'language', 'course_category', 'course', 'section', 'sub_section', 'quiz', 'question'
        )
    
admin.site.register(Answers, AnswerAdmin)



# User Marks
class AdminUserMarks(admin.ModelAdmin):
    list_display = ('user',
                    'language',
                    'course_category',
                    'course',
                    'section',
                    'sub_section',
                    'quiz'
                    )
    readonly_fields = ('slug',)
    list_filter     = ('user',
                      'language',
                      'course_category',
                      'course',
                      'section',
                      'sub_section',
                      )
    search_fields   = ('user',
                      'language',
                      'course_category',
                      'course',
                      'section',
                      'sub_section',
                      )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related(
            'language', 'course_category', 'course', 'section', 'sub_section', 'quiz'
        )
admin.site.register(UserMarks, AdminUserMarks)