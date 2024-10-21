from django.db import models
from django.utils import timezone
from courses_app.models import Language, Course_Category, Course, User
# Create your models here.
class CouponCode(models.Model):
    code            = models.CharField(max_length=50, unique=True)
    is_active       = models.BooleanField(default=True, help_text='0 - Non Active, 1 - Active')
    valid_from      = models.DateTimeField(auto_now_add=True)
    valid_to        = models.DateTimeField()
    usage_count     = models.PositiveIntegerField(default=0)
    usage_limit     = models.PositiveIntegerField(default=1)


    class Meta:
        verbose_name        = 'Coupon Code'
        verbose_name_plural = 'Coupon Codes'

    def __str__(self):
        return self.code


class CoursesPurchased(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    language            = models.ForeignKey(Language, on_delete=models.CASCADE)
    course_category     = models.ForeignKey(Course_Category, on_delete=models.CASCADE)
    course              = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name        = 'Course Purchased'
        verbose_name_plural = 'Courses Purchased'

    def __str__(self):
        return f'{self.course}-{self.user}'
