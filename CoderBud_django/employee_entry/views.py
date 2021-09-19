from django.shortcuts import redirect, render
from .forms import EmployeeTaDaForm
from .models import TADA
# Create your views here.

def tada_list(request):
    context ={'tada_list':TADA.objects.all()}
    return render(request,"tada_entry/tada_list.html",context) 

def tada_form(request):
    if request.method == "GET":
        form = EmployeeTaDaForm()
        return render(request,"tada_entry/tada_form.html", {'form':form})
    else:
        form = EmployeeTaDaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/tada/list')
