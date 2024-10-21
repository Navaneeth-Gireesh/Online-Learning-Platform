from django.db import models
from django.contrib.auth.models import User
import datetime
import os
from courses_app.models import Language

# Function to save Profile Pictures
def profile_picture_upload_to(instance, filename):
    user_name       = instance.user.username.replace(" ", "_").replace("/", "_")
    now_time        = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name, ext  = os.path.splitext(filename)
    new_file_name   = f"{now_time}_{base_name}_{user_name}{ext}"
    return f"User_Management/Profile_Pictures/{user_name}_{new_file_name}"

# Profile Model
class Profile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'), 
        ('Female', 'Female'),
        ('Transgender', 'Transgender'), 
        ('Other', 'Other')
    ]

    EDUCATION_CHOICES = [
        ('Below 10th', 'Below 10th'),
        ('10th', '10th'),
        ('12th', '12th'),
        ('Diploma', 'Diploma'),
        ('Graduate', 'Graduate'),
        ('Under Graduate', 'Under Graduate'),
        ('Post Graduate', 'Post Graduate')
    ]

    OCCUPATIONAL_CHOICES = [
        ('Student', 'Student'),
        ('Employed', 'Employed'),
        ('Unemployed', 'Unemployed'),
        ('Others', 'Others')
    ]

    user                    = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture         = models.ImageField(upload_to=profile_picture_upload_to, default='User_Management/Profile_Pictures/Default/profile_pic_default.jpg')
    mobile_number           = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth           = models.DateField(blank=True, null=True)
    language                = models.ForeignKey(Language, on_delete=models.CASCADE,null=True, blank=True, help_text="Select a Language for Course")
    location                = models.CharField(max_length=100, blank=True, null=True, help_text="Enter your Current Location")
    gender                  = models.CharField(max_length=12, choices=GENDER_CHOICES, blank=True, null=True)
    education               = models.CharField(max_length=20, choices=EDUCATION_CHOICES, blank=True, null=True)
    occupational_status     = models.CharField(max_length=10, choices=OCCUPATIONAL_CHOICES, blank=True, null=True)

