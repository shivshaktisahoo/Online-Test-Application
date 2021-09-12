from django.db import models
from student.models import *

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=30)
    def __str__(self):
        return self.course_name

class Subject(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=30)
    total_marks = models.PositiveIntegerField()
    def __str__(self):
        return self.subject_name

options = [
    ('option1','option1'),
    ('option2','option2'),
    ('option3','option3'),
    ('option4','option4')]
class Question(models.Model):
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.CharField(choices=options,max_length=100)
    ques_mark = models.PositiveIntegerField()

class Performance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    obtained_mark = models.IntegerField()
    total_marks = models.PositiveIntegerField()