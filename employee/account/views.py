from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,FormView,CreateView
from django.views import View
from django.forms import BaseModelForm
from .forms import LogForm,RegForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy

# Create your views here.



class LandingView(TemplateView):
    template_name="index.html"


class LoginView(FormView):
    template_name="log.html"
    form_class=LogForm
    def post(self,request):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pwd=form_data.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                messages.success(request,"login successful")
                return redirect('chome')
            else:
                messages.error(request,"login failed")
                return redirect('log')
        return render(request,"log.html",{"form":form_data})


class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    success_url=reverse_lazy("log")
    def form_valid(self, form: BaseModelForm):
        messages.success(self.request,"registration successful")
        return super().form_valid(form)
    def form_invalid(self, form: BaseModelForm):
        messages.error(self.request,"registration failed")
        return super().form_invalid(form)

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('landing')

