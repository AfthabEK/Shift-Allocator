import datetime,csv
from django.shortcuts import render
from .models import *
from .forms import *
from datetime import datetime
from django.shortcuts import redirect
from datetime import date, timedelta
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def addemployee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        id = request.POST.get('id')
        type = request.POST.get('type')
        temp = Employee(emp_id=id, type=type, name=name)
        temp.save()
        return render(request, 'homepage.html')
    return render(request, 'addemployee.html', {'form': EmployeeForm})

