from django.urls import path, include
from . import AdminViews, UserViews

urlpatterns = [
    # ------------------------------------------------ ADMIN URLS ---------------------------------------------

    # ADMIN ----Language
    path('Admin/Course-Languages/Languages/Create',AdminViews.admin_course_languages_create, name = 'admin_course_languages_create'),
    path('Admin/Course-Languages/Languages/Edit/<slug:language_slug>', AdminViews.admin_course_language_edit, name = 'admin_course_language_edit'),
    path('Admin/Course-Languages/Language/Delete/<slug:language_slug>', AdminViews.admin_course_language_delete, name = 'admin_course_language_delete'),

    # ADMIN ----Course Category
    path('Admin/Course-Category/View/<slug:language_slug>', AdminViews.admin_language_course_category_view, name = 'admin_language_course_category_view'),
    path('Admin/Course-Category/Create/<slug:language_slug>', AdminViews.admin_course_category_create, name = 'admin_course_category_create'),
    path('Admin/Course-Category/Edit/<slug:category_slug>/', AdminViews.admin_course_category_edit, name='admin_course_category_edit'),
    path('Admin/Course-Category/Delete/<slug:category_slug>', AdminViews.admin_course_category_delete, name = 'admin_course_category_delete'),

    #ADMIN ----Courses
    path('Admin/Courses/View/<slug:category_slug>', AdminViews.admin_course_view, name = 'admin_course_view'),
    path('Admin/Courses/Create/<slug:category_slug>', AdminViews.admin_course_create, name = 'admin_course_create'),
    path('Admin/Courses/Edit/<slug:course_slug>', AdminViews.admin_course_edit, name = 'admin_course_edit'),
    path('Admin/Courses/Delete/<slug:course_slug>', AdminViews.admin_course_delete, name = 'admin_course_delete'),

    #ADMIN ---- Course Info
    path('Admin/Courses/Info/View/<slug:course_slug>', AdminViews.admin_course_info, name = 'admin_course_info'),
    path('Admin/Courses/Info/Create/<slug:course_slug>', AdminViews.admin_course_info_create, name = 'admin_course_info_create'),
    path('Admin/Courses/Info/Edit/<slug:course_info_slug>', AdminViews.admin_course_info_edit, name = 'admin_course_info_edit'),
    path('Admin/Courses/Info/Delete/<slug:course_info_slug>', AdminViews.admin_course_info_delete, name ='admin_course_info_delete'),

    #ADMIN ---- Course Trailer
    path('Admin/Courses/Trailer/View/<slug:course_slug>', AdminViews.admin_course_trailer_view, name='admin_course_trailer_view'),
    path('Admin/Courses/Trailer/Create/<slug:course_slug>', AdminViews.admin_course_trailer_create, name ='admin_course_trailer_create'),
    path('Admin/Courses/Trailer/Edit/<slug:course_trailer_slug>', AdminViews.admin_course_trailer_edit, name ='admin_course_trailer_edit'),
    path('Admin/Courses/Trailer/Delete/<slug:course_trailer_slug>', AdminViews.admin_course_trailer_delete, name = 'admin_course_trailer_delete'),
    #ADMIN ---- Section
    path('Admin/Courses/Section/View/<slug:course_slug>', AdminViews.admin_course_section_view, name = 'admin_course_section_view'),
    path('Admin/Courses/Section/Create/<slug:course_slug>', AdminViews.admin_course_section_create, name = 'admin_course_section_create'),
    path('Admin/Courses/Section/Edit/<slug:section_slug>', AdminViews.admin_course_section_edit, name = 'admin_course_section_edit'),
    path('Admin/Courses/Section/Delete/<slug:section_slug>', AdminViews.admin_course_section_delete, name ='admin_course_section_delete'),

    #ADMIN ---- Sub Section
    path('Admin/Courses/Sub-Section/View/<slug:section_slug>', AdminViews.admin_course_sub_section_view, name = 'admin_course_sub_section_view'),
    path('Admin/Courses/Sub-Section/Create/<slug:section_slug>', AdminViews.admin_course_sub_section_create, name = 'admin_course_sub_section_create'),
    path('Admin/Courses/Sub-Section/Edit/<slug:sub_section_slug>', AdminViews.admin_course_sub_section_edit, name ='admin_course_sub_section_edit'),
    path('Admin/Courses/Sub-Section/Delete/<slug:sub_section_slug>', AdminViews.admin_course_sub_section_delete, name = 'admin_course_sub_section_delete'),
    
    #ADMIN ---- Video
    path('Admin/Courses/Video/View/<slug:sub_section_slug>', AdminViews.admin_course_video_view, name ='admin_course_video_view'),
    path('Admin/Courses/Video/Create/<slug:sub_section_slug>', AdminViews.admin_course_video_create, name = 'admin_course_video_create'),
    path('Admin/Courses/Video/Edit/<slug:video_slug>', AdminViews.admin_course_video_edit, name ='admin_course_video_edit'),
    path('Admin/Courses/Video/Delete/<slug:video_slug>', AdminViews.admin_course_video_delete, name = 'admin_course_video_delete'),
    

    #ADMIN ---- Documents
    path('Admin/Courses/Documents/View/<slug:video_slug>', AdminViews.admin_video_document_view, name ='admin_video_document_view'),
    path('Admin/Courses/Documents/Creare/<slug:video_slug>', AdminViews.admin_video_document_create, name = 'admin_video_document_create'),
    path('Admin/Courses/Documents/Edit/<slug:document_slug>', AdminViews.admin_video_document_edit, name ='admin_video_document_edit'),
    path('Admin/Courses/Documents/Delete/<slug:document_slug>', AdminViews.admin_video_document_delete, name= 'admin_video_document_delete'),
    
    # ------------------------------------------------ STUDENT URLS ---------------------------------------------
    # USER ---- Languages
    path('User/Languages/View', UserViews.user_languages_view, name = 'user_languages_view'),

    # USER ---- Course Categories & Courses
    path('User/Categories_&_Courses/View/<slug:language_slug>', UserViews.user_course_categories_and_courses, name = 'user_course_categories_and_courses'),
    
    # USER ---- Course Data
    path('User/Course_Data/view/<slug:course_slug>', UserViews.course_data, name = 'course_data'),

]
