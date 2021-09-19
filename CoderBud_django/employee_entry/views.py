from django.shortcuts import redirect, render
from .forms import EmployeeTaDaForm
from .models import TADA
# Create your views here.

def tada_list(request):
    context ={'tada_list':TADA.objects.all()}
    return render(request,"tada_entry/tada_list.html",context) 

def tada_form(request, id = 0):
    if request.method == "GET":
        if id== 0:
            form = EmployeeTaDaForm()
        else:
            tada = TADA.objects.get(pk=id)
            form = EmployeeTaDaForm(instance = tada)
        return render(request,"tada_entry/tada_form.html", {'form':form})
    else:
        if id == 0:
            form = EmployeeTaDaForm(request.POST)
        else:
            tada = TADA.objects.get(pk=id)
            form = EmployeeTaDaForm(request.POST, instance = tada)
        if  form.is_valid():
            form.save()
        return redirect('/tada/list')

def tada_delete(request,id):
    tada = TADA.objects.get(pk=id)
    tada.delete()
    return redirect('/tada/list')