from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from.models import Question
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
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
    cool =Question.objects.all()
    return render (request,'question/index.html',{'cool':cool})
    return HttpResponseRedirect('/')
