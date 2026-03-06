from django.urls import path
from .views import get_departments, add_department

urlpatterns = [
    path('departments/', get_departments, name='get-departments'),
    path('departments/add/', add_department, name='add-department'),
]

