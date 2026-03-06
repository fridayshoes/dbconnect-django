from django.urls import path
from .views import delete_department, get_department_id, get_departments, add_department, delete_department

urlpatterns = [
    path('departments/', get_departments, name='get-departments'),
    path('departments/add/', add_department, name='add-department'),
    path('departments/delete/<int:id>/', delete_department, name='delete-department'),
    path('getdepartment_id/<int:id>/', get_department_id, name='get-department-id'),
]

