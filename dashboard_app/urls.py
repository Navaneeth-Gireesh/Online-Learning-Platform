from django.urls import path
from . import views

urlpatterns = [

    # --- Admin Dashboard Starts ---

    # ADMIN ---- Users
    path('Admin/Users/All-Users/', views.all_users , name = 'all_users'),
    path('Admin/Users/All-Users-Teachers/', views.all_teacher_users, name = 'all_teacher_users'),
    path('Admin/Users/All-Users-Students/', views.all_student_users, name = 'all_student_users'),
    path('Admin/Users/All-Users-Admins/', views.all_admin_users, name = 'all_admin_users'),
    path('Admin/Users/All-Non-Active-Users/', views.all_non_active_users, name = 'all_non_active_users'),

    # ADMIN ---- Courses
    path('Admin/Course-Languages/All-Languages', views.all_languages, name='all_languages'),

    # --- Admin Dashboard Ends ---
]