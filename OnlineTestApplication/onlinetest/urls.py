from django.urls import path

from .views import *
app_name = 'onlinetest'


urlpatterns = [
        path('coursesubjectview/',course_subject_view,name='course_subject_view'),
        path('courselist/',course_list,name='course_list'),
        path('courseupdate/<int:id>',course_update,name='course_update'),
        path('addnewcourse/',add_new_course,name='add_new_course'),
        
        path('subjectlist/',subject_list,name='subject_list'),
        path('subjectupdate/<int:id>',subject_update,name='subject_update'),
        path('subjectdelete/<int:id>/',subject_delete, name='subject_delete'),
        path('addnewsubject/',add_new_subject,name='add_new_subject'),

        path('questionview/',question_view,name='question_view'),
        path('questionlist/',question_list,name='question_list'),
        path('questionupdate/<int:id>',question_update,name='question_update'),
        path('questiondelete/<int:id>/',question_delete, name='question_delete'),
        path('addnewquestion/',add_new_question,name='add_new_question'),
]