from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import studentsSerializer
from .models import students

@api_view(['GET'])
def list_students(request):
    students_instance = students.objects.all()
    serializer = studentsSerializer(students_instance, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def create_student(request):
    
    serializer = studentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def retrieve_student(request, pk):
    try:
        students_instance = students.objects.get(id=pk)
        serializer = studentsSerializer(students_instance, many=False)
    
        return Response(serializer.data)
    except students.DoesNotExist:
        return Response({"detail": "student not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_student(request, pk):
    students_instance = students.objects.get(id=pk)
    serializer = studentsSerializer(instance=students_instance, data=request.data,  partial = True, many=False)
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_student(request, pk):
    students_instance = get_object_or_404(students, id=pk)
    students_instance.delete()
    
    return Response('Item successfully deleted')