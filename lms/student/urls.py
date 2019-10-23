from django.urls import path
from .views import *
urlpatterns = [
    path('register',student_register, name="student_register")
]