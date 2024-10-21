from django import forms
from .models import Language, Course_Category, Course, Course_Info, Course_Trailer, Section, Sub_Section, Video, Document

# ---------------------------------- ADMIN -----------------------------------


# Language Create Form
class CourseLanguageCreateForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = [
            'language',
        ]
        labels = {
            'language'      :'Language',
        }

# Course Category Create Form
class CourseCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Course_Category
        fields = [
            'language',
            'name',
            'description'
        ]
        labels = {
            'language'      : 'Language',
            'name'          : 'Name',
            'description'   : 'Description'
        }

# Course Create Form
class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'language',
            'category',
            'title',
            'thumbnail',
            'original_price',
            'discount_price',
            'description',
            'instructors',
            'course_active',
            'trending'
        ]
        labels = {
            'language' : 'Language',
            'category' : 'Category',
            'title' : 'Title',
            'thumbnail' : 'Thumbnail',
            'original_price' : 'Original Price',
            'discount_price' : 'Discount Price',
            'description' : 'Description',
            'instructors' : 'Instructors',
            'course_active' : 'Course Status',
            'trending' : 'Trending Status'
        }

# Course Info Create Form
class CourseInfoCreateForm(forms.ModelForm):
    class Meta:
        model = Course_Info
        fields = [
            'language',
            'category',
            'course',
            'outcomes',
            'offerings',
            'order'
        ]
        labels = {
            'language' : 'Language',
            'category' : 'Category',
            'course' : 'Course',
            'outcomes' : 'Outcomes',
            'offerings' : 'Offerings',
            'order': 'Order'
        }


# Course Trailer Create Form
class CourseTrailerCreateForm(forms.ModelForm):
    class Meta:
        model = Course_Trailer
        fields = [
            'language',
            'category',
            'course',
            'title',
            'video_file',
            'thumbnail',
            'order'
        ]
        labels = {
            'language' : 'Language',
            'category' : 'Category',
            'course' : 'Course',
            'title' : 'Title',
            'video_file' :'Video File Link',
            'thumbnail' : 'Thumbnail Link',
            'order' : 'Order'
        }

# Course Section Create form
class CourseSectionCreateForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = [
            'language',
            'category',
            'course',
            'title',
            'order'
        ]
        labels = {
            'language': 'Language',
            'category' : 'Category',
            'course' : 'Course',
            'title' : 'Title',
            'order' : 'Order'
            
        }

# Course Sub Section Create Form
class CourseSubSectionCreateForm(forms.ModelForm):
    class Meta:
        model = Sub_Section
        fields = [
            'language',
            'category',
            'course',
            'section',
            'title',
            'order'
        ]
        labels = {
            'language' : 'Language',
            'category' : 'Category',
            'course' : 'Course',
            'section': 'Section',
            'title' : 'Title',
            'order' : 'Order'
        }

# Course Video Create Form
class CourseVideoCreateForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            'language',
            'category',
            'course',
            'section',
            'sub_section',
            'title',
            'video_file',
            'thumbnail',
            'demo',
            'order'
        ]
        labels = {
            'language' : 'Language',
            'category' : 'Category',
            'course' : 'Course',
            'section' : 'Section',
            'sub_section' : 'Sub Section',
            'title' : 'Title',
            'video_file' : 'Video File',
            'thumbnail' : 'Thumbnail',
            'demo' : 'Demo',
            'order' : 'Order'
        }

# Course Document Create Form
class CourseDocumentCreateForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'language',
            'category',
            'course',
            'section',
            'sub_section',
            'video',
            'title',
            'document',
            'order'
        ]
        labels = {
            'language' : 'Language',
            'category' : 'Category',
            'course' : 'Course',
            'section' : 'Section',
            'sub_section' : 'Sub Section',
            'video' : 'Video',
            'title' : 'Title',
            'document' : 'Document',
            'order' : 'Order'
        }