from django import forms
from django.contrib.auth.forms import UserCreationForm, User
from .models import Student


class StudentForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Full Name'}),label='Full Name')
    dob = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}),label='Date of Birth')
    profile_photo = forms.ImageField()
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your Address'}),label='Address')
    contactno = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Contact No.'}),label='Contact No.')
    class Meta:
        model = Student
        fields = ['full_name','dob', 'profile_photo','address', 'contactno']

