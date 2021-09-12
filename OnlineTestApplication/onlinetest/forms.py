from django import forms
from .models import *


class CourseForm(forms.ModelForm):
    course_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Add new course'}),label='Add New Course')
    class Meta:
        model = Course
        fields = "__all__"

class SubjectForm(forms.ModelForm):
    # course_name = forms.Select(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Select course'}),label='Course')
    subject_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Add new subject'}),label='Add New Subject')
    total_marks = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter total marks'}),label='Total marks')
    class Meta:
        model = Subject
        fields = "__all__"
        widgets = {
            'course_name': forms.Select(attrs={'class': 'custom-select'}),
        }
        labels = {
            'course_name': 'Course',
        }

class QuestionForm(forms.ModelForm):
    # subject_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Select Subject'}),label='Subject')
    question = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'put question here'}),label='Question')
    option1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First option'}),label='Option 1')
    option2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'second option'}),label='Option 2')
    option3 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'third option'}),label='Option 3')
    option4 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'fourth option'}),label='Option 4')
    ques_mark = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'mark for this question'}),label='Mark for this question')
    class Meta:
        model = Question
        fields = "__all__"
        widgets = {
            'subject_name': forms.Select(attrs={'class': 'custom-select'}),
            'correct_option': forms.Select(attrs={'class': 'custom-select'}),
        }
        labels = {
            'subject_name': 'Subject',
            'correct_option': 'Correct Option',
        }
