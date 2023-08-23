from django.contrib import admin
from .models import Emp,Testimonial,Feedback
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','emp_id','address')
    list_editable=('address',)
    search_fields=('name',)
    list_filter=('working','department')
    
class TestimonialAdmin(admin.ModelAdmin):
    list_display=('name','testimonial','picture','rating')


class FeedbackAdmin(admin.ModelAdmin):
    list_display=('name','email','feedback')
    search_fields=('name','email')



admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial,TestimonialAdmin)
admin.site.register(Feedback,FeedbackAdmin)