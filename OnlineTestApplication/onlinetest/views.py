from django.shortcuts import render, redirect
from .forms import *
from .models import *
from teacher.models import Teacher
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
# Create your views here.


@user_passes_test(lambda u: u.is_teacher and u.is_verified)
def course_subject_view(request):
    course = "active"
    teach = Teacher.objects.filter(user=request.user).first() 
    return render(request, 'onlinetest/course_subject_view.html',locals())

# Related to Courses
@user_passes_test(lambda u: u.is_teacher and u.is_verified)
def course_list(request):
    course = "active"
    teach = Teacher.objects.filter(user=request.user).first() 
    courselist = Course.objects.all()
    return render(request, 'onlinetest/course_list.html', locals())

@user_passes_test(lambda u: u.is_teacher and u.is_verified)
def course_update(request, id):
    course = "active"
    teach = Teacher.objects.filter(user=request.user).first()
    object_ = Course.objects.filter(id=id).first()
    form = CourseForm(instance=object_)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=object_)
        if form.is_valid():
            form.save()
            messages.success(request, "Course Updated Successfully")
            return redirect('onlinetest:course_list')
        else:
            messages.error(request, "Please Provide valid data")
    return render(request, 'onlinetest/course_update.html', locals())

@user_passes_test(lambda u: u.is_teacher and u.is_verified)
def add_new_course(request):
    course = "active"
    teach = Teacher.objects.filter(user=request.user).first()
    form = CourseForm()
    if request.method=='POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"CONFIRMED !!!!")
            return redirect('onlinetest:course_subject_view')
    return render(request, 'onlinetest/add_new_course.html', locals())

# Related to Subjects
@user_passes_test(lambda u: u.is_teacher and u.is_verified)
def subject_list(request):
    course = "active"
    teach = Teacher.objects.filter(user=request.user).first() 
    subjectlist = Subject.objects.all()
    return render(request, 'onlinetest/subject_list.html', locals())

@user_passes_test(lambda u: u.is_teacher and u.is_verified)
def subject_update(request, id):
    course = "active"
    teach = Teacher.objects.filter(user=request.user).first()
    object_ = Subject.objects.filter(id=id).first()
    form = SubjectForm(instance=object_)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=object_)
        if form.is_valid():
            form.save()
            messages.success(request, "Subject Updated Successfully")
            return redirect('onlinetest:subject_list')
        else:
            messages.error(request, "Please Provide valid data")
    return render(request, 'onlinetest/subject_update.html', locals())

@user_passes_test(lambda u: u.is_teacher and u.is_verified)
def subject_delete(request, id):
    Subject.objects.filter(id=id).first().delete()
    return redirect('onlinetest:subject_list')

@user_passes_test(lambda u: u.is_teacher and u.is_verified)
def add_new_subject(request):
    course = "active"
    teach = Teacher.objects.filter(user=request.user).first()
    form = SubjectForm()
    if request.method=='POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"CONFIRMED !!!!")
            return redirect('onlinetest:course_subject_view')
    return render(request, 'onlinetest/add_new_subject.html', locals())

@user_passes_test(lambda u: u.is_teacher and u.is_verified)
def question_view(request):
    ques = "active"
    teach = Teacher.objects.filter(user=request.user).first() 
    return render(request, 'onlinetest/question_view.html',locals())

@user_passes_test(lambda u: u.is_teacher and u.is_verified)
def question_list(request):
    ques = "active"
    teach = Teacher.objects.filter(user=request.user).first() 
    questionlist = Question.objects.all()
    return render(request, 'onlinetest/question_list.html', locals())

@user_passes_test(lambda u: u.is_teacher and u.is_verified)
def question_update(request, id):
    ques = "active"
    teach = Teacher.objects.filter(user=request.user).first()
    object_ = Question.objects.filter(id=id).first()
    form = QuestionForm(instance=object_)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=object_)
        if form.is_valid():
            form.save()
            messages.success(request, "Subject Updated Successfully")
            return redirect('onlinetest:question_list')
        else:
            messages.error(request, "Please Provide valid data")
    return render(request, 'onlinetest/question_update.html', locals())

@user_passes_test(lambda u: u.is_teacher and u.is_verified)
def question_delete(request, id):
    Question.objects.filter(id=id).first().delete()
    return redirect('onlinetest:question_list')

@user_passes_test(lambda u: u.is_teacher and u.is_verified)
def add_new_question(request):
    ques = "active"
    teach = Teacher.objects.filter(user=request.user).first()
    form = QuestionForm()
    if request.method=='POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"CONFIRMED !!!!")
            return redirect('onlinetest:question_view')
    return render(request, 'onlinetest/add_new_question.html', locals())