from django.urls import path
from . import UserViews, AdminViews

urlpatterns = [
    # ------------------------------------------------ STUDENT URLS ---------------------------------------------
    # USER ---- Purchases
    path('Course/Buy_Now/<slug:course_slug>', UserViews.buy_now, name = 'buy_now'),
    path('Course/Coupon/Invalid_Coupon_Code', UserViews.invalid_coupon_code, name = 'invalid_coupon_code'),
    path('Course/Purchase_Course/<slug:course_slug>', UserViews.user_purchase_course, name = 'user_purchase_course'),
    path('Course/My_Learnings', UserViews.user_my_learnings, name = 'user_my_learnings'),


    # ------------------------------------------------ ADMIN URLS ------------------------------------------------
    # ADMIN ---- Coupons
    path('Admin/Coupons', AdminViews.admin_coupons_view, name = 'admin_coupons_view'),
    path('Admin/Coupons_Create', AdminViews.admin_coupon_create, name = 'admin_coupon_create'),
    path('Admin/Coupon_Edit/<int:coupon_id>',AdminViews.admin_coupon_edit, name = 'admin_coupon_edit'),
    path('Admin/Coupon_Delete/<int:coupon_id>', AdminViews.admin_coupon_delete, name = 'admin_coupon_delete'),

    # ADMIN ---- USERS
    path('Admin/Users/Enrolled_Courses/<int:user_id>', AdminViews.admin_user_enrolled_courses_view, name = 'admin_user_enrolled_courses_view'),
]