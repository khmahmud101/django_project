from django import forms
from .models import Article
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class createform(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            
            'title',
            'body',
            'image',
            'category',
        ]

class registerUser(UserCreationForm):
    class Meta:
        model = User
        fields=[
            
            'username',
            'email',
            

        ]