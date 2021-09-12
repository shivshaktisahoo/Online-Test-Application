from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from teacher.models import *
from student.models import *
from .models import User

# Create your views here.
def home(request):
    return render(request, 'main/base.html')


def signup(request, category):
    if request.user.is_authenticated:
        if user.is_teacher:
            return redirect('teacher:profile')
        else:
            return redirect('student:profile')
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if category == 'teacher':
                form.is_teacher = True
                form.save()
                Teacher.objects.create(user=form)
                return redirect('main:teacher_signin')
            else:
                form.is_student = True
                form.save()
                Student.objects.create(user=form)
                return redirect('main:student_signin')
            # messages.success(request, "User Saved Successfully")
            # form = SignupForm()
        else:
            messages.error(request, "Please Provide valid data")

    return render(request, 'main/signup.html', locals())


def teacher_signin(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['pass']
        user = authenticate(username=username, password=password)
        if user and user.is_verified and user.is_teacher:
            login(request, user)
            messages.success(request, f"Welcome, {username}")
            return redirect('teacher:profile')
        else:
            messages.error(request, 'Please Provide Valid Username / Password')
    if request.user.is_authenticated and request.user.is_verified and request.user.is_teacher:
        return redirect('teacher:profile')
    return render(request, 'main/teacher_signin.html')


def student_signin(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['pass']
        user = authenticate(username=username, password=password)
        if user and user.is_verified and user.is_student:
            login(request, user)
            messages.success(request, f"Welcome, {username}")
            return redirect('student:profile')
        else:
            messages.error(request, 'Please Provide Valid Username / Password')
        if request.user.is_authenticated and request.user.is_verified and request.user.is_student:
            return redirect('student:profile')
    return render(request, 'main/student_signin.html')

def signout(request):
    request.session.flush()
    logout(request)
    return redirect('main:home')