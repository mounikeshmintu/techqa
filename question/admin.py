from django.contrib import admin
from .models import Category,Question
from .forms import QuestionForm
# from django import models
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
admin.site.register( Question)
admin.site.register( Category)
