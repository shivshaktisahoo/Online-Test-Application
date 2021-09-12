from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from .models import Student
from onlinetest.models import *
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
@user_passes_test(lambda u: u.is_student and u.is_verified)
def student_profile(request):
    dashboard = 'active'
    stu = Student.objects.filter(user=request.user).first()
    return render(request, 'student/student_profile.html', locals()) 

@user_passes_test(lambda u: u.is_student and u.is_verified)
def edit_student(request, id):
    dashboard = 'active'
    stu = Student.objects.filter(user=request.user).first()  
    object_ = Student.objects.filter(id=id).first()
    form = StudentForm(instance=object_)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES,
                          instance=object_)
        if form.is_valid():
            form.save()
            messages.success(request, "Object Updated Successfully")
            return redirect('student:profile')
        else:
            messages.error(request, "Please Provide valid data")

    return render(request, 'student/studentprofile_update.html', locals())

@user_passes_test(lambda u: u.is_student and u.is_verified)
def view_test(request):
    ques = 'active'
    stu = Student.objects.filter(user=request.user).first()
    subject = Subject.objects.all()
    return render(request, 'student/view_test.html', locals()) 

@user_passes_test(lambda u: u.is_student and u.is_verified)
def take_test(request, id):
    ques = 'active'
    stu = Student.objects.filter(user=request.user).first()
    questions = Question.objects.filter(subject_name=id)
    sub_name = questions[0].subject_name
    print(sub_name)
    print(questions)
    return render(request, 'student/take_test.html', locals())

@user_passes_test(lambda u: u.is_student and u.is_verified)
def get_answer(request):
    try:
        data = request.GET
        print(data)
        for i in data:
            print(data[i])
        id = int(data['id'])
        print(id,type(id))
        questions = Question.objects.filter(subject_name=id)
        print(questions)
        dict1 = dict()
        for i in data:
            dict1[i] =  data[i]
        print(type(dict1))
        for i in dict1:
            print(dict1[i])
        print(dict1)
        dict1.pop("id")
        print(dict1)
        stu_obtain_mark = 0
        total_mark = 0
        for i,j in zip(questions,dict1):
            # print(dict1[j],type(dict1[j]))
            # print(i.correct_option,type(i.correct_option))
            if dict1[j] == i.correct_option:
                stu_obtain_mark += i.ques_mark    
            else:
                print('False')
            total_mark += i.ques_mark
        print(stu_obtain_mark)
        print(total_mark)
        sub_name = questions[0].subject_name
        sub = Subject.objects.filter(subject_name=sub_name).first()
        print(sub,type(sub))
        stu = Student.objects.filter(user=request.user).first()
        print(stu,type(stu))
       
        stu_perf = Performance.objects.create(student=stu,
                                            subject_name=sub,
                                            obtained_mark=stu_obtain_mark,
                                            total_marks=total_mark)
        stu_perf.save()
    except:
        pass
    return redirect('student:student_performance')

@user_passes_test(lambda u: u.is_student and u.is_verified)
def student_performance(request):
    perfomance = 'active'
    stu = Student.objects.filter(user=request.user).first()
    stu_perf = Performance.objects.filter(student=stu)
    return render(request, 'student/student_performance.html', locals())