from django.contrib import admin
from . models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display        = ('get_username', 'get_first_name', 'get_last_name','date_of_birth', 'mobile_number', 'date_of_birth', 'location', 'gender')
    list_filter         = ('gender', 'location', 'education', 'occupational_status',)
    search_fields       = ('user__username','user__first_name','user__last_name','mobile_number')

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'
    
    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'
    
    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'
admin.site.register(Profile, ProfileAdmin)