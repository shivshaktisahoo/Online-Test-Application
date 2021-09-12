from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'dob','profile_photo','address','contactno')

admin.site.register(Student,StudentAdmin)
