from .models import Employee, DateWindow, WeekStructure
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id', 'type', 'name']

