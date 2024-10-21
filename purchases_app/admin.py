from django.contrib import admin
from . models import CouponCode, CoursesPurchased
# Register your models here.


class CouponCodeAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'valid_from',
        'valid_to',
        'usage_count',
        'usage_limit',
        'is_active'
    ]
    
admin.site.register(CouponCode, CouponCodeAdmin)

class CoursesPurchasedAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'course',
        'language',
        'course_category',
    ]
admin.site.register(CoursesPurchased, CoursesPurchasedAdmin)
