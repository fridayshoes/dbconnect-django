from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Department
from .serializers import DepartmentSerializer
 
@api_view(['GET'])
def get_departments(request):
    departments = Department.objects.all().values()
    return Response(list(departments))
 
 
@api_view(['POST'])
def add_department(request):
 
    serializer = DepartmentSerializer(data=request.data)
 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
 
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_department(request, id):
    try:
        department = Department.objects.get(dept_id=id)
        department.delete()
        return Response({"message": "Department deleted successfully"})
    except Department.DoesNotExist:
        return Response({"error": "Department not found"})
    
@api_view(['GET'])
def get_department_id(request, id):
    try:
        department = Department.objects.get(dept_id=id)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)
    except Department.DoesNotExist:
        return Response({"error": "Department id not found"})
 
 