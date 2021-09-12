from django.contrib import admin
from .models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','course_name')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id','course_name','subject_name','total_marks')
    list_filter = ('course_name','subject_name') 

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','subject_name','question','correct_option','ques_mark')
    list_filter = ('subject_name',)

class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('id','student','subject_name','obtained_mark','total_marks')
    list_filter = ('student','subject_name')  

admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Performance, PerformanceAdmin)