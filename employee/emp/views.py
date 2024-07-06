from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views import View
from .forms import EmpForm 
from django.contrib import messages
from .models import EmpData


# Create your views here.
class HomeView(TemplateView):
    template_name="home.html"


class EmployeeView(View):
    def get(self,request):
        form=EmpForm()
        return render(request,"addemp.html",{"form":form})
    def post(self,request):
        form_data=EmpForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"employee added successfully")
            return redirect('elist')
        messages.error(request,"employee adding failed")
        return render(request,"addemp.html",{"form":form_data})
    
class EmpListView(View):
    def get(self,request):
        edata=EmpData.objects.all()
        return render(request,"emplist.html",{"employee":edata})
    

class RemoveEmpView(View):
    def get (self,request,*args,**kwargs):
        try:
            eid=kwargs.get('eid')
            edata=EmpData.objects.get(id=eid)
            edata.delete()
            messages.success(request,"deleted")
            return redirect('elist')
        except:
            messages.error(request,"deletion failed")
            return redirect('elist')
        
class EditEmpView(View):
    def get (self,request,*args,**kwargs):
        eid=kwargs.get('eid')
        edata=EmpData.objects.get(id=eid)
        form=EmpForm(instance=edata)
        return render(request,"editemp.html",{"form":form})
    def post(self,request,*args,**kwargs):
        eid=kwargs.get('eid')
        edata=EmpData.objects.get(id=eid)
        form_data=EmpForm(data=request.POST,instance=edata)
        if form_data.is_valid():
            form_data.save()
            return redirect('elist')
        return render(request,"editemp.html",{"form":form_data})
