from django.shortcuts import redirect, render
from .forms import EmployeeTaDaForm
from .models import TADA
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas, textobject
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter 



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
    textob.setFont("Helvetica", 14)



    tadas =TADA.objects.all()

    lines = []
    lines.append("Date          Name            Travel Cost         Lunch Cost          Instrument Cost         Paid")
    for tada in tadas:
        lines.append(str(tada.date) + "            " + str(tada.employee_name) + "           " + str(tada.travel_cost) + "         " + str(tada.lunch_cost) + "          " + str(tada.instruments_cost) + "            " + str(tada.paid))
        lines.append("________________________________________________________________________________________________")

    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='tada.pdf')

      