from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from .models import Teacher
from onlinetest.models import *
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

@user_passes_test(lambda u: u.is_teacher and u.is_verified)
def teacher_profile(request):
    dashboard = 'active'
    teach = Teacher.objects.filter(user=request.user).first()  
    return render(request, 'teacher/teacher_profile.html', locals())    

@user_passes_test(lambda u: u.is_teacher and u.is_verified)
def edit_teacher(request, id):
    dashboard = 'active'
    teach = Teacher.objects.filter(user=request.user).first()  
    object_ = Teacher.objects.filter(id=id).first()
    form = TeacherForm(instance=object_)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES,
                          instance=object_)
        if form.is_valid():
            form.save()
            messages.success(request, "Object Updated Successfully")
            return redirect('teacher:profile')
        else:
            messages.error(request, "Please Provide valid data")

    return render(request, 'teacher/teacherprofile_update.html', locals())

@user_passes_test(lambda u: u.is_teacher and u.is_verified)
def check_student_performance(request):
    perfomance = 'active'
    teach = Teacher.objects.filter(user=request.user).first()
    stu_perf = Performance.objects.all()
    return render(request, 'teacher/check_student_performance.html', locals())