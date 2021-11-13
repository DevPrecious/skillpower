from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'state', 'organization', 'profile_image']

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name_of_school','address', 'state', 'number_of_students', 'courses_to_offer', 'additional_information']

class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ['name_of_office','address', 'state', 'number_of_staffs', 'courses_to_offer', 'additional_information']

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['address', 'state', 'courses_to_offer', 'additional_information']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_class', 'age', 'course_to_take']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'department', 'age', 'course_to_take']