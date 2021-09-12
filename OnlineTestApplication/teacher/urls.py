from django.urls import path

from .views import *
app_name = 'teacher'


urlpatterns = [
        # path('',teacher,name='teacher'),
        path('profile/',teacher_profile,name='profile'),
        path('edit/<int:id>/', edit_teacher, name='edit_teacher'),
        path('checkstudentperformance/',check_student_performance,name="check_student_performance"),
]