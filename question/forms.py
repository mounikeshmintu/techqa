from .models import *
from django import forms
class QuestionForm(forms.ModelForm):

    class Meta:


        model=Question
        # model=Category

        fields=('name','description','category')
