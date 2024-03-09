from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TeachersSerializer
from .models import Teachers

@api_view(['GET'])
def list_teachers(request):
    teachers_instance = Teachers.objects.all()
    serializer = TeachersSerializer(teachers_instance, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def create_teacher(request):
    
    serializer = TeachersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET']) 
def retrieve_teacher(request, pk):
    try:
        teachers_instance = Teachers.objects.get(id=pk)
        serializer = TeachersSerializer(teachers_instance, many=False)
    
        return Response(serializer.data)
    except Teachers.DoesNotExist:
        return Response({"detail": "teacher not found"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def update_teacher(request, pk):
    teachers_instance = Teachers.objects.get(id=pk)
    serializer = TeachersSerializer(instance=teachers_instance, data=request.data,  partial = True, many=False)
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_teacher(request, pk):
    teachers_instance = get_object_or_404(Teachers, id=pk)
    teachers_instance.delete()
    
    return Response('Item successfully deleted')
    

