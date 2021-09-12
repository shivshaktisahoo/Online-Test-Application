from django.urls import path
from .views import *
app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('signup/<str:category>/', signup, name='signup'),
    path('teachersignin/',teacher_signin,name='teacher_signin'),
    path('studentsignin/',student_signin,name='student_signin'),
    path('signout/', signout, name='signout'),

]