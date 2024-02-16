from django.shortcuts import render


from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import AdministratorsSerializer
from .models import Administrators

@api_view(['GET'])
def list_administrators(request):
    administrators_instance = Administrators.objects.all()
    serializer = AdministratorsSerializer(administrators_instance, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def create_administrator(request):
    
    serializer = AdministratorsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def retrieve_administrator(request, pk):
    try:
        administrators_instance = Administrators.objects.get(id=pk)
        serializer = AdministratorsSerializer(administrators_instance, many=False)
    
        return Response(serializer.data)
    except Administrators.DoesNotExist:
        return Response({"detail": "administrator not found"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def update_administrator(request, pk):
    administrators_instance = Administrators.objects.get(id=pk)
    serializer = AdministratorsSerializer(instance=administrators_instance, data=request.data,  partial = True, many=False)
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_administrator(request, pk):
    administrators_instance = get_object_or_404(Administrators, id=pk)
    administrators_instance.delete()
    
    return Response('Item successfully deleted')