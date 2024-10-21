from django.urls import path
from . import UserViews, AdminViews

urlpatterns = [
    path('registration/', UserViews.user_registration, name = 'user_registration'),
    path('registration_otp_validate/', UserViews.registration_otp_validate, name = 'registration_otp_validate'),

    path('login/', UserViews.user_login, name = 'user_login'),
    path('logout/', UserViews.user_logout, name = 'user_logout'),

    path('profile_view/', UserViews.profile_view, name = 'profile_view'),
    path('profile_edit_details/', UserViews.profile_edit_details, name = 'profile_edit_details'),

    path('forgot_password/', UserViews.forgot_password, name = 'forgot_password'),
    path('forgot_password/password_reset_otp/', UserViews.password_reset_otp, name = 'password_reset_otp'),
    path('forgot_password/password_reset_form/', UserViews.password_reset_form, name = 'password_reset_form'),


   # ------------------------------- ADMIN USERS MANAGEMENT -----------------------------------------

   path('Admin/Users/User_Edit/<int:user_id>', AdminViews.user_edit, name = 'user_edit')
]