from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="front-page"),


    path('register/', views.registerPage, name="register"),
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),


    path('home/', views.homePage, name="home"),
    path('profile/', views.profile, name="profile"),
    path('school-detail/', views.school, name="school-detail"),
    path('office-detail/', views.office, name="office-detail"),
    path('community-detail/', views.community, name="community-detail"),
    path('add-student/', views.addStudent, name="add-student"),
    path('add-staff/', views.addStaff, name="add-staff"),
    path('test/', views.testpage, name="test"),
]
