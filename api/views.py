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
 