from .models import *
from django import forms
class UserRegistrationForm(forms.Form):
    
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )




















# class QuestionForm(forms.ModelForm):
#
#     class Meta:
#
#
#         model=Question
#         # model=Category
#
#         fields=('name','description','category')
