from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_employee, name='add_employee'),
    # Add other URL patterns as needed
]
