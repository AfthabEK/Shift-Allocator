from django.db import models


class Employee(models.Model):
    EMPLOYEE_TYPES = (
        ('assistant', 'Library Assistant'),
        ('helper', 'Library Helper'),
        ('digital', 'Digital Library Employee'),
    )
    emp_id = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=EMPLOYEE_TYPES)
    name= models.CharField(max_length=50)
    def __str__(self):
        return self.emp_id

class DateWindow(models.Model):
    start_date = models.DateField()

    def __str__(self):
        return self.start_date.strftime("%d/%m/%Y")

class WeekStructure(models.Model):
    SHIFT_TYPES = (
        ('general', 'General'),
        ('morning', 'Morning'),
        ('night', 'Night'),
        ('off', 'Off'),
    )
    date_window = models.ForeignKey(DateWindow, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    mon = models.CharField(max_length=10, choices=SHIFT_TYPES)
    tue = models.CharField(max_length=10, choices=SHIFT_TYPES)
    wed = models.CharField(max_length=10, choices=SHIFT_TYPES)
    thu = models.CharField(max_length=10, choices=SHIFT_TYPES)
    fri = models.CharField(max_length=10, choices=SHIFT_TYPES)
    sat = models.CharField(max_length=10, choices=SHIFT_TYPES)
    sun = models.CharField(max_length=10, choices=SHIFT_TYPES)

    def __str__(self):
        
        return self.employee.emp_id+" "+self.date_window.start_date.strftime("%d/%m/%Y")

