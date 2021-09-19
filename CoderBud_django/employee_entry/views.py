from django.shortcuts import redirect, render
from .forms import EmployeeTaDaForm
from .models import TADA
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas, textobject
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter 
from django.db.models import Sum


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

def generate_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf,pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica", 10)



    tadas =TADA.objects.all()

  
    travel_cost_sum = TADA.objects.aggregate(Sum('travel_cost'))
    total_travel_cost = travel_cost_sum['travel_cost__sum']

    lunch_cost_sum = TADA.objects.aggregate(Sum('lunch_cost'))
    total_lunch_cost = lunch_cost_sum['lunch_cost__sum']

    instruments_cost_sum = TADA.objects.aggregate(Sum('instruments_cost'))
    total_instruments_cost = instruments_cost_sum['instruments_cost__sum']

    #net_cost = float(str(total_travel_cost))+float(str(total_lunch_cost))+float(str(total_instruments_cost))
    net_cost = total_travel_cost+total_lunch_cost+total_instruments_cost
    lines = []
    
    lines.append("Date                      Name            Travel Cost         Lunch Cost          Instrument Cost         Paid")
    for tada in tadas:
        lines.append(str(tada.date) + "            " + str(tada.employee_name) + "                " + str(tada.travel_cost) + "               " + str(tada.lunch_cost) + "                       " + str(tada.instruments_cost) + "                   " + str(tada.paid))
        lines.append("_______________________________________________________________________")

    lines.append("")
    lines.append("Total travel cost:" + str(total_travel_cost))
    lines.append("")
    lines.append("Total lunch cost:" + str(total_lunch_cost))
    lines.append("")
    lines.append("Total instruments cost:" + str(total_instruments_cost))
    lines.append("")
    lines.append("Net cost:" + str(net_cost))
   
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='tada.pdf')

      