from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'emp_id','type']  # Add other fields as needed
