from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
# Create your views here.

class ContactFormView(FormView):
    template_name = 'app/contact.html'
    form_class = ContactForm
    success_url = '/thankyou/'
    initial = {'name':'Ashish','email':'ashish@gmail.com','msg':'Hii bro'}
    def form_valid(self,form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        return super().form_valid(form)

class ThankyouFormView(TemplateView):
    template_name = 'app/thankyou.html'
    form_class = ContactForm