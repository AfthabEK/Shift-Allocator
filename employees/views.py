
from django.shortcuts import render, redirect
from .forms import EmployeeForm

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
         # Redirect to a list view
    else:
        form = EmployeeForm()

    return render(request, 'employees/add_employee.html', {'form': form})

