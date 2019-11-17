from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name="index"),
    path('profile/<name>',profile,name="profile"),
    path('single/<int:id>',single_post,name="single_post"),
    path('category/<name>',category,name="category"),
    path('login',getlogin,name="login"),
    path('logout',getlogout,name="logout"),
    path('create',create,name="create"),
    path('author_profile',author_profile,name="author_profile"),
    path('update/<int:id>',getupdate,name="update"),
    path('delete/<int:id>',getdelete,name="delete"),
    path('register',getregister,name="register"),
    
    
]
