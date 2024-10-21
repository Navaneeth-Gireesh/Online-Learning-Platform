from django.contrib import admin
from . models import Course_Category, Language, Course, Course_Info
from . models import Section, Sub_Section,  Video, Document, Course_Trailer

# Register your models here.


# Language Admin
class LanguageAdmin(admin.ModelAdmin):
    list_display        = ('language', 'slug')
    readonly_fields     = ('slug',)
    list_filter         = ('language',)
    search_fields       = ('language',)

admin.site.register(Language, LanguageAdmin)


# Course Category Admin
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display        = ('name', 'slug')
    readonly_fields     = ('slug',)
    list_filter         = ('name',)
    search_fields       = ('name',)

admin.site.register(Course_Category, CourseCategoryAdmin)


# Course Admin
class CourseAdmin(admin.ModelAdmin):
    list_display        = ('title', 'slug', 'language', 'category',
                            'original_price', 'discount_price',
                              'created_at', 'updated_at' , 'course_active', 'trending')
    readonly_fields     = ('slug',)
    list_filter         = ('category', 'instructors','language',)
    search_fields       = ('category', 'instructors','language',)

admin.site.register(Course, CourseAdmin)

# Course Info Admin
class CourseInfoAdmin(admin.ModelAdmin):
    list_display        = ('category', 'language', 'course','order')
    readonly_fields     = ('slug',)
    list_filter         = ('category','language', 'course',)
    search_fields       = ('category','language', 'course',)

admin.site.register(Course_Info,CourseInfoAdmin)


# Section Admin
class SectionAdmin(admin.ModelAdmin):
    list_display        = ('category','language', 'course', 'title', 'order')
    readonly_fields     = ('slug',)
    list_filter         = ('category','language', 'course',)
    search_fields       = ('category','language', 'course',)

admin.site.register(Section, SectionAdmin)

# Sub Section Admin
class SubSectionAdmin(admin.ModelAdmin):
    list_display        = ('category','language', 'course','section', 'title', 'order')
    readonly_fields     = ('slug',)
    list_filter         = ('category','language', 'course','section',)
    search_fields       = ('category','language', 'course','section',)

admin.site.register(Sub_Section, SubSectionAdmin)

# Course Trailer Admin
class CourseTrailerAdmin(admin.ModelAdmin):
    list_display        = ('category','language', 'course', 'title', 'order')
    readonly_fields     = ('slug',)
    list_filter         = ('category','language', 'course',)
    search_fields       = ('category','language', 'course',)

admin.site.register(Course_Trailer, CourseTrailerAdmin)

# Video Admin
class VideoAdmin(admin.ModelAdmin):
    list_display        = ('title', 'category', 'language', 'course', 'section','sub_section', 'order')
    readonly_fields     = ('slug',)
    list_filter         = ('category', 'language', 'course', 'section','sub_section',)
    search_fields       = ('category', 'language', 'course', 'section','sub_section',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related(
            'category','language', 'course', 'section', 'sub_section'
        )

admin.site.register(Video, VideoAdmin)

# Document Admin
class DocumentAdmin(admin.ModelAdmin):
    list_display        = ('title', 'category', 'language', 'course', 'section','sub_section','video', 'order')
    readonly_fields     = ('slug',)
    list_filter         = ('category', 'language', 'course', 'section','sub_section',)
    search_fields       = ('category', 'language', 'course', 'section','sub_section',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related(
            'category','language', 'course', 'section', 'sub_section'
        )

admin.site.register(Document, DocumentAdmin)