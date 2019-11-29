from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView

from HSSapp.models import User


class RegForm(ModelForm):
    class Meta():
        model=User
        fields=['username','password','email','phone','state','district','area']


class reg(CreateView):
    model = User
    fields = ['username', 'password', 'email', 'phone', 'state', 'district', 'area']
    template_name = 'HSSapp/registration.html'
    success_url = reverse_lazy('home')

    # def get(self,request,*args,**kwargs):
    #     context={}
    #     context['form']=self.form_class
    #     return render(request,self.template_name,context=context)
    #
    # def post(self,request,*args,**kwargs):
    #     form=self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('register')