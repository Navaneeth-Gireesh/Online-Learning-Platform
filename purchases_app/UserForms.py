from django import forms
from . models import CoursesPurchased
from . tasks import send_course_purchase_email_task

class CoursesPurchasedForm(forms.ModelForm):
    class Meta:
        model = CoursesPurchased
        fields = [
            'user',
            'language',
            'course_category',
            'course'
        ]

    def send_email(self):
        user_instance = self.cleaned_data['user']
        language_instance = self.cleaned_data['language']
        course_category_instance = self.cleaned_data['course_category']
        course_instance = self.cleaned_data['course']

        send_course_purchase_email_task.delay( 
            email           = user_instance.email,    
            language        = language_instance.language, 
            course_category = course_category_instance.name, 
            course          = course_instance.title 
        )
