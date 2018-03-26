"""techqa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic.base import TemplateView
from .views import Create,Home
from django.urls import reverse
from .models import Question
app_name='main'

urlpatterns = [
    # url(r'^/',views.home,name='home'),
    url(r'^home/',Home,name='home'),
    url(r'^ques/',Create.as_view(success_url="/index/home/"),name='ques')
    # CreateView.as_view(model=myModel, success_url=reverse('success-url'))

]
