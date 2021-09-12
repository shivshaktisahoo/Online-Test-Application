from django.contrib import admin
from .models import Teacher

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'dob','profile_photo','address','contactno')

admin.site.register(Teacher, TeacherAdmin)