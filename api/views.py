from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from student.models import Student
from student.serializers import StudentCreateSerializer, StudentSerializer



@api_view(['GET'])
def students(request):
    query_index_number = request.GET.get('index_number')
    if query_index_number is None:
        students =  Student.objects.all()       
    else:
        students = Student.objects.all().filter(username=query_index_number)
    serializer = StudentSerializer(instance=students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_student(request):
    serializer = StudentCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance=serializer.save()
        print(serializer.data)
        data = serializer.data
        return Response(data)
    
    

    