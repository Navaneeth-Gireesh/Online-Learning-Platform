from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# import datetime
# import os

# Create your models here.

# --------------------------------------- Functions ----------------------------------------

# # Function to save Thumbnails
# def course_thumbnails_upload_to(instance, filename):
#     course_category     = instance.category.name.replace(" ","_").replace("/","_")
#     language            = instance.language.language.replace(" ","_").replace("/","_")
#     course_title        = instance.title.replace(" ","_").replace("/","_")
#     now_time            = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#     base_name, ext      = os.path.splitext(filename)
#     new_file_name       = f"{now_time}{ext}"
#     return f"Courses_App/{course_category}/{language}/{course_title}/Thumbnails/{new_file_name}"

# # Function to save Course Trailers
# def course_trailer_upload_to(instance, filename):
#     course_category     = instance.category.name.replace(" ","_").replace("/","_")
#     language            = instance.language.language.replace(" ","_").replace("/","_")
#     course              = instance.course.title.replace(" ","_").replace("/","_")
#     now_time            = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#     base_name, ext      = os.path.splitext(filename)
#     new_file_name       = f"{now_time}{ext}"
#     return f"Courses_App/{course_category}/{language}/{course}/Trailers/{new_file_name}"

# # Function to save Video and Document Files
# def file_upload_to(instance, filename):
#     course_category     = instance.category.name.replace(" ", "_").replace("/", "_")
#     language            = instance.language.language.replace(" ", "_").replace("/", "_")
#     course              = instance.course.title.replace(" ", "_").replace("/", "_")
#     section             = instance.section.title.replace(" ", "_").replace("/", "_")
#     sub_section         = instance.sub_section.title.replace(" ", "_").replace("/", "_")
#     now_time            = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#     base_name, ext      = os.path.splitext(filename)
#     new_file_name       = f"{now_time}{ext}"
#     return f"Courses_App/{course_category}/{language}/{course}/{section}/{sub_section}/{new_file_name}"

# # Function to save Video Thumbnail Files
# def video_thumbnail_file_upload_to(instance, filename):
#     course_category     = instance.category.name.replace(" ", "_").replace("/", "_")
#     language            = instance.language.language.replace(" ", "_").replace("/", "_")
#     course              = instance.course.title.replace(" ", "_").replace("/", "_")
#     section             = instance.section.title.replace(" ", "_").replace("/", "_")
#     sub_section         = instance.sub_section.title.replace(" ", "_").replace("/", "_")
#     now_time            = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#     base_name, ext      = os.path.splitext(filename)
#     new_file_name       = f"{now_time}{ext}"
#     return f"Courses_App/{course_category}/{language}/{course}/{section}/{sub_section}/{new_file_name}"






# --------------------------------------- Models ----------------------------------------


# Course Language Model
class Language(models.Model):
    """ Model representing the Languages """
    language                        = models.CharField(max_length=100, help_text="Enter a Language")
    slug                            = models.SlugField(max_length=255,unique=True, blank=True, null=True)

    class Meta:
        verbose_name                = "Language"
        verbose_name_plural         = "Languages"

    def save(self, *args, **kwargs):
        if not self.slug or not self.pk:
            self.slug               = slugify(f'{self.language}')
        else:
            current_language        = Language.objects.filter(pk=self.pk).first()
            if current_language:
                if (self.language   != current_language.language):
                    self.slug       = slugify(f'{self.language}')
        if not self.slug:
            self.slug               = slugify(f'{self.language}')
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.language




# Course Category Model
class Course_Category(models.Model):
    """ Model representing a course category or type, such as 'Coding', 'Language' etc.."""
    language        = models.ForeignKey(Language, on_delete=models.CASCADE, help_text="Select a Language")
    name            = models.CharField(max_length=250, help_text= "Enter the category name (e.g., 'Coding', 'Language' etc..)")
    slug            = models.SlugField(max_length=255,unique=True, blank=True)
    description     = models.TextField(help_text="Give a brief description for the category")
    
    class Meta:
        verbose_name            = "Course Category"
        verbose_name_plural     = "Course Categories"

    def save(self, *args, **kwargs):
        if not self.slug or not self.pk:  
            self.slug               = slugify(f'{self.language}-{self.name}')
        else:
            current_category        = Course_Category.objects.filter(pk=self.pk).first()
            if current_category:
                if (self.name       != current_category.name or
                    self.language   != current_category.language):
                    self.slug       = slugify(f'{self.language}-{self.name}')
        

        if not self.slug:
            self.slug               = slugify(f'{self.language}-{self.name}')
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"




# Courses Model
class Course(models.Model):
    """Model representing the courses"""
    language        = models.ForeignKey(Language, on_delete=models.CASCADE, help_text="Select the Language")
    category        = models.ForeignKey(Course_Category, on_delete=models.CASCADE, help_text="Select a Category")
    title           = models.CharField(max_length=250, help_text="Title of the course")
    slug            = models.SlugField(max_length=255,unique=True, blank=True, null=True)
    thumbnail       = models.URLField(help_text="Give a Thumbnail URL for this course")
    original_price  = models.IntegerField(default=0, help_text="0 Means Free Course")
    discount_price  = models.IntegerField(default=0, help_text="0 Means Free Course")
    description     = models.TextField(help_text="Description or brief of the course")
    instructors     = models.ManyToManyField(User, limit_choices_to={'is_staff': True}, help_text="Select the Instructors of the Course")
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    course_active   = models.BooleanField(default=True, help_text="Course is active or not")
    trending        = models.BooleanField(default=False, help_text="Trending Course or not")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


    def save(self, *args, **kwargs):
        if not self.slug or not self.pk:
            self.slug               = slugify(f'{self.language}-{self.category}-{self.title}')
        else:
            current_course          = Course.objects.filter(pk=self.pk).first()
            if current_course:
                if (self.language   != current_course.language or
                    self.category   != current_course.category or
                    self.title      != current_course.title):

                    self.slug       = slugify(f'{self.language}-{self.category}-{self.title}')
        if not self.slug:
            self.slug               = slugify(f'{self.language}-{self.category}-{self.title}')

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"



class Course_Info(models.Model):
    """Model representing Course Info"""
    language        = models.ForeignKey(Language, on_delete=models.CASCADE, help_text="Select the Language")
    category        = models.ForeignKey(Course_Category, on_delete=models.CASCADE, help_text="Select the Category")
    course          = models.ForeignKey(Course, on_delete=models.CASCADE, help_text="Select the Course")
    slug            = models.SlugField(max_length=255,unique=True, blank=True, null=True)
    outcomes        = models.TextField(null=True, blank=True, help_text="The Outcome a Student gets")
    offerings       = models.TextField(null=True, blank=True, help_text="What we offer for this course after completion")
    order           = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Course Info"
        verbose_name_plural = "Course Infos"
    
    def save(self, *args, **kwargs):
        if not self.slug or not self.pk:
            self.slug               = slugify(f'{self.language}-{self.category}-{self.course}-{self.order}')
        else:
            current_course_info = Course_Info.objects.filter(pk=self.pk).first()
            if current_course_info:
                if (self.language   != current_course_info.language or
                    self.category   != current_course_info.category or
                    self.course     != current_course_info.course or
                    self.order      != current_course_info.order):

                    self.slug       = slugify(f'{self.language}-{self.category}-{self.course}-{self.order}')
        if not self.slug:
            self.slug               = slugify(f'{self.language}-{self.category}-{self.course}-{self.order}')

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course}"
    

# Course Trailer Video
class Course_Trailer(models.Model):
    """ Model representing the Course Trailer of a Course """
    language            = models.ForeignKey(Language, on_delete=models.CASCADE, help_text="Select the Language")
    category            = models.ForeignKey(Course_Category, on_delete=models.CASCADE, help_text="Select the Category")
    course              = models.ForeignKey(Course, on_delete=models.CASCADE, help_text="Select the Course")
    title               = models.CharField(max_length=250, help_text="Give a title to the Course")
    slug                = models.SlugField(max_length=255,unique=True, blank=True, null=True)
    video_file          = models.URLField(help_text="Give the Video file URL")
    thumbnail           = models.URLField(help_text="Give the Thumbnail URL")
    order               = models.PositiveIntegerField()
    
    class Meta:
        verbose_name            = "Course Trailer"
        verbose_name_plural     = "Course Trailers"
        unique_together         = ('course','order')
        ordering                = ['course','order']

    def save(self, *args, **kwargs):
        if not self.slug or not self.pk:
            self.slug                   = slugify(f'{self.language}-{self.category}-{self.course}-{self.title}')
        else:
            current_course_trailer      = Course_Trailer.objects.filter(pk=self.pk).first()
            if current_course_trailer:
                if (self.language       != current_course_trailer.language or
                    self.category       != current_course_trailer.category or
                    self.course         != current_course_trailer.course or 
                    self.title          != current_course_trailer.title):

                    self.slug           = slugify(f'{self.language}-{self.category}-{self.course}-{self.title}')
        if not self.slug:
            self.slug                   = slugify(f'{self.language}-{self.category}-{self.course}-{self.title}')
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



# Section Model
class Section(models.Model):
    """ Model representing the sections of a course """
    language    = models.ForeignKey(Language, on_delete=models.CASCADE, help_text="Select the Language")
    category    = models.ForeignKey(Course_Category, on_delete=models.CASCADE, help_text="Select the Category")
    course      = models.ForeignKey(Course, on_delete=models.CASCADE, help_text="Select the Course")
    title       = models.CharField(max_length=250, help_text="Give a title to the Section")
    slug        = models.SlugField(max_length=255,unique=True, blank=True, null=True)
    order       = models.PositiveIntegerField()

    class Meta:
        verbose_name            = "Section"
        verbose_name_plural     = "Sections"
        unique_together         = ('course','order')
        ordering                = ['course','order']

    def save(self, *args, **kwargs):
        if not self.slug or not self.pk:
            self.slug                   = slugify(f'{self.language}-{self.category}-{self.course}-{self.title}')
        else:
            current_section             = Section.objects.filter(pk=self.pk).first()
            if current_section:
                if (self.language       != current_section.language or
                    self.category       != current_section.category or
                    self.course         != current_section.course or 
                    self.title          != current_section.title):

                    self.slug           = slugify(f'{self.language}-{self.category}-{self.course}-{self.title}')
        if not self.slug:
            self.slug                   = slugify(f'{self.language}-{self.category}-{self.course}-{self.title}')
        
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title



# Sub-Section Model
class Sub_Section(models.Model):
    """ Model representing the Sub Section of a Section of a course """
    language        = models.ForeignKey(Language, on_delete=models.CASCADE, help_text="Select the Language")
    category        = models.ForeignKey(Course_Category, on_delete=models.CASCADE, help_text="Select the Category")
    course          = models.ForeignKey(Course, on_delete=models.CASCADE, help_text="Select the Course")
    section         = models.ForeignKey(Section, on_delete=models.CASCADE, help_text="Select the Section")
    title           = models.CharField(max_length=250, help_text="Give a title to the Sub Section")
    slug            = models.SlugField(max_length=255,unique=True, blank=True, null=True)
    order           = models.PositiveIntegerField()

    class Meta:
        verbose_name            = "Sub Section"
        verbose_name_plural     = "Sub Sections"
        unique_together         = ('section','order')
        ordering                = ['section','order']
    
    def save(self,*args, **kwargs):
        if not self.slug or not self.pk:
            self.slug                       = slugify(f'{self.language}-{self.category}-{self.course}-{self.section}-{self.title}')
        else:
            selected_sub_section            = Sub_Section.objects.filter(pk=self.pk).first()
            if selected_sub_section:
                if (self.language           != selected_sub_section.language or
                    self.category           != selected_sub_section.category or
                    self.course             != selected_sub_section.course or
                    self.section            != selected_sub_section.section or
                    self.title              != selected_sub_section.title):

                    self.slug               = slugify(f'{self.language}-{self.category}-{self.course}-{self.section}-{self.title}')
        if not self.slug:
            self.slug                       = slugify(f'{self.language}-{self.category}-{self.course}-{self.section}-{self.title}')

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    


# Video Model
class Video(models.Model):
    language            = models.ForeignKey(Language, on_delete=models.CASCADE, help_text="Select the Language")
    category            = models.ForeignKey(Course_Category, on_delete=models.CASCADE, help_text="Select the Category")
    course              = models.ForeignKey(Course, on_delete=models.CASCADE, help_text="Select the Course")
    section             = models.ForeignKey(Section, on_delete=models.CASCADE, help_text="Select the Section")
    sub_section         = models.ForeignKey(Sub_Section, on_delete=models.CASCADE, help_text="Select the Sub Section")
    title               = models.CharField(max_length=250, help_text="Give a title to the Video")
    slug                = models.SlugField(max_length=255,unique=True, blank=True, null=True)
    video_file          = models.URLField(help_text="Give the Video file URL")
    thumbnail           = models.URLField(help_text="Give the Thumbnail URL")
    demo                = models.BooleanField(default=False, help_text="If its a demo video users will be able to view it without purchasing the course")
    order               = models.PositiveIntegerField()

    class Meta:
        verbose_name            = "Video"
        verbose_name_plural     = "Videos"
        unique_together         = ('sub_section','order')
        ordering                = ['sub_section','order']

    def save(self, *args, **kwargs):
        if not self.slug or not self.pk:
            self.slug                   = slugify(f'{self.language}-{self.category}-{self.course}-{self.section}-{self.sub_section}-{self.title}')
        else:
            current_video               = Video.objects.filter(pk=self.pk).first()
            if current_video:
                if (self.language       != current_video.language or
                    self.category       != current_video.category or
                    self.course         != current_video.course or
                    self.section        != current_video.section or
                    self.sub_section    != current_video.sub_section or
                    self.title          != current_video.title):

                    self.slug           = slugify(f'{self.language}-{self.category}-{self.course}-{self.section}-{self.sub_section}-{self.title}')
        if not self.slug:
            self.slug                   = slugify(f'{self.language}-{self.category}-{self.course}-{self.section}-{self.sub_section}-{self.title}')
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



# Document Model
class Document(models.Model):
    language            = models.ForeignKey(Language, on_delete=models.CASCADE, help_text="Select the Language")
    category            = models.ForeignKey(Course_Category, on_delete=models.CASCADE, help_text="Select the Category")
    course              = models.ForeignKey(Course, on_delete=models.CASCADE, help_text="Select the Course")
    section             = models.ForeignKey(Section, on_delete=models.CASCADE, help_text="Select the Section")
    sub_section         = models.ForeignKey(Sub_Section, on_delete=models.CASCADE, help_text="Select the Sub Section")
    video               = models.ForeignKey(Video, on_delete=models.CASCADE, help_text="Select the Video")
    title               = models.CharField(max_length=250, help_text="Give a title to the Document")
    slug                = models.SlugField(max_length=255,unique=True, blank=True, null=True)
    document            = models.URLField(help_text='Give the Document URL')
    demo                = models.BooleanField(default=False, help_text="If its a demo Document users will be able to view it without purchasing")
    order               = models.PositiveIntegerField()

    class Meta:
        verbose_name            = "Document"
        verbose_name_plural     = "Documents"
        unique_together         = ('video','order')
        ordering                = ['video','order']
    

    def save(self, *args, **kwargs):
        if not self.slug or not self.pk:
            self.slug                   = slugify(f'{self.language}-{self.category}-{self.course}-{self.section}-{self.sub_section}-{self.video}-{self.title}')
        else:
            current_document            = Document.objects.filter(pk=self.pk).first()
            if current_document:
                if (self.language       != current_document.language or
                    self.category       != current_document.category or
                    self.course         != current_document.course or
                    self.section        != current_document.section or
                    self.sub_section    != current_document.sub_section or
                    self.video          != current_document.video or
                    self.title          != current_document.title):

                    self.slug           = slugify(f'{self.language}-{self.category}-{self.course}-{self.section}-{self.sub_section}-{self.video}-{self.title}')
        if not self.slug:
            self.slug                   = slugify(f'{self.language}-{self.category}-{self.course}-{self.section}-{self.sub_section}-{self.video}-{self.title}')

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

