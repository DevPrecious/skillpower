from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import *
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# def index(request):
#     context = {
#         'title' : 'Skill Power'
#     }
#     return render(request, 'skill/frontpage.html',  context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Account was created for {user}')

                return redirect('login')

        content = {
            'title' : 'Register',
            'form' : form
        }
        return render(request, 'skill/register.html', content)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,  user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
                

        context = {
            'title' : 'Login'
        }
        return render(request, 'skill/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def homePage(request):
    students = Student.objects.filter(school=request.user).count()
    staffs = Staff.objects.filter(office=request.user).count()
    context = {
        'title' : 'Skillpower - dashboard',
        'students' : students,
        'staffs' : staffs,
    }
    return render(request, 'skill/home.html', context)

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, use_required_attribute=False, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, use_required_attribute=False,  
                                        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('profile')
        elif u_form.is_valid() and request.user.profile.organization != "":
            u_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(use_required_attribute=False, instance=request.user)
        p_form = ProfileUpdateForm(use_required_attribute=False, instance=request.user.profile)
    
    context = {
        'title' : 'Profile Page',
        'u_form' : u_form,
        'p_form' : p_form
    }

    return render(request, 'skill/profile.html', context)


def school(request):
    if request.user.profile.organization == "Community" or  request.user.profile.organization == "Office":
        return redirect('home')
    if request.method == 'POST':
        form = SchoolForm(request.POST, use_required_attribute=False, instance=request.user.school)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
            messages.success(request, 'Uploaded')
            return redirect('school-detail')
    else:
        form = SchoolForm(use_required_attribute=False, instance=request.user.school)
    
    context = {
        'title' : 'School',
        'form' : form
    }
    return render(request, 'skill/school.html', context)

def office(request):
    if request.user.profile.organization == "Community" or  request.user.profile.organization == "School":
        return redirect('home')
    if request.method == 'POST':
        form = OfficeForm(request.POST, use_required_attribute=False, instance=request.user.office)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
            messages.success(request, 'Uploaded')
            return redirect('office-detail')
    else:
        form = OfficeForm(use_required_attribute=False, instance=request.user.office)
    
    context = {
        'title' : 'Office',
        'form' : form
    }
    return render(request, 'skill/office.html', context)


def community(request):
    if request.user.profile.organization == "School" or  request.user.profile.organization == "Office":
        return redirect('home')
    if request.method == 'POST':
        form = CommunityForm(request.POST, use_required_attribute=False, instance=request.user.community)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
            messages.success(request, 'Uploaded')
            return redirect('community-detail')
    else:
        form = CommunityForm(use_required_attribute=False, instance=request.user.community)
    
    context = {
        'title' : 'Community',
        'form' : form
    }
    return render(request, 'skill/community.html', context)

def testpage(request):
    context = {
        'title' : 'Title'
    }
    return render(request, 'skill/test.html', context)

def addStudent(request):
    if request.user.profile.organization == "Office" or  request.user.profile.organization == "Community":
        return redirect('home')
    if request.method == 'POST':
        form = StudentForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.school = request.user
            instance.save()
            messages.success(request, 'Student Registered')
            return redirect('add-student')
    else:
        form = StudentForm(use_required_attribute=False)
    context = {
        'title' : 'Register a student',
        'form' : form
    }
    return render(request, 'skill/addstudent.html', context)


def addStaff(request):
    if request.user.profile.organization == "School" or  request.user.profile.organization == "Community":
        return redirect('home')
    if request.method == 'POST':
        form = StaffForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.office = request.user
            instance.save()
            messages.success(request, 'Staff Registered')
            return redirect('add-student')
    else:
        form = StaffForm(use_required_attribute=False)
    context = {
        'title' : 'Register a staff',
        'form' : form
    }
    return render(request, 'skill/addstaff.html', context)