from django.contrib import admin

# Register your models here.
from .models import Employee, DateWindow, WeekStructure

admin.site.register(Employee)
admin.site.register(DateWindow)
admin.site.register(WeekStructure)

