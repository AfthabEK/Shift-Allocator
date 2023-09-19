from django.db import models

# Create your models here.


class Employee(models.Model):
    EMPLOYEE_TYPES = (
        ('assistant', 'Library Assistant'),
        ('helper', 'Library Helper'),
        ('digital', 'Digital Library Employee'),
    )
    emp_id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=10, choices=EMPLOYEE_TYPES)
    name= models.CharField(max_length=50)
    def __str__(self):
        return self.emp_id
    
