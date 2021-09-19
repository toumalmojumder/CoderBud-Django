from django import forms
from django import forms
from .models import TADA


class DateInput(forms.DateInput):
    input_type = 'date'

class EmployeeTaDaForm(forms.ModelForm):
    class Meta:
        model = TADA
        fields = '__all__'
        widgets = {
            'date': DateInput(),
            
        }
    def __init__(self, *args,**kwargs):
        super(EmployeeTaDaForm,self).__init__( *args,**kwargs)
        self.fields['employee_name'].empty_label = "(Select here)"
        self.fields['paid'].empty_label = "(Select here)"
