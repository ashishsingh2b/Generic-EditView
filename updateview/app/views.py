from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from  .models import Student
from django.views.generic.base import TemplateView
# Create your views here.

class StudentCreateView(CreateView):
    model = Student
    fields = ['name','email','password']
    success_url = '/thankyou/'

class Thankyouview(TemplateView):
    template_name = 'app/thankyou.html'

class StudentUpdateview(UpdateView):
    model = Student
    fields = ['name','email','password']
    success_url = '/thankyou/'

class StudentDeleteview(DeleteView):
    model = Student
    success_url = '/thankyou/'