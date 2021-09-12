from django.urls import path
from .views import *
app_name = 'student'


urlpatterns = [
        # path('',student,name='student'),
        path('profile/',student_profile,name='profile'),
        path('edit/<int:id>/', edit_student, name='edit_student'),
        path('viewtest/',view_test,name="view_test"),
        path('taketest/<int:id>/',take_test,name="take_test"),
        path('getanswer/',get_answer,name="get_answer"),
        path('studentperformance/',student_performance,name="student_performance"),
]