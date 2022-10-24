from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        # fields = ['name','last_name','email']
        # Si son todos seria '__all__'
        extra_fields=['salary']
        #Tambien podria solo excluir
        exclude = ('email',)