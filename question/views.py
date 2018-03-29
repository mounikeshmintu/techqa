from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from.models import Question
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models import Q

from django.db.models import Q

# Create your views here.

class Create(CreateView):
    model=Question
    fields=['name','description','category']
    template_name='question/ques.html'
    def test_redirect(request):
        return redirect('home')
    # def ok(request):
    #
    #     return HttpResponse("your question has been succesfull added")
    # if request.POST:
    #
    # else:

# class Home(DetailView):
#     model=Question
#     template_name='question/index.html'
#     def get_context_data(self,*args,**kwargs):
#         context=super(Home,self).get_context_data(*args,**kwargs)
#         context['cool']=Question.objects.all()
#         return context
def Home(request):
    cool =Question.objects.order_by('name')
    return render (request,'question/index.html',{'cool':cool})
    return HttpResponseRedirect('/')
# def signup(request):
#     form=UserRegistrationForm()
#     if request.method=='POST':
#
#         if form.is_valid():
#             userobj=form.cleaned_data
#             username=userobj['Username']
#             email=userobj['Email']
#             password=userobj['Password']
#             if not User.objects.filter(username=username).exists():
#                 User.objects.create_user(username,email,password)
#                 user=authenticate(username=username,password=password)
#                 login(request,user)
#             else:
#                 raise forms.ValidationError("looks like username already exist ")
#         else:
#             raise forms.ValidationError("looks like username already exist ")
#
#     else :
#         form=UserRegistrationForm()
#     return render(request, 'question/signup.html', {'form' : form})
def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

    else:
        form = UserRegistrationForm()

    return render(request, 'question/signup.html', {'form' : form})
def Search(request):


    # if 'q' in request.get == 'q'and request.get['q']:
    query=request.GET.get('q')

    results= Question.objects.filter(name__icontains=query)
    return render(request,'question/search.html',{'res':results,'q':query})
