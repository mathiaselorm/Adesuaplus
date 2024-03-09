from . models import Teachers
from rest_framework import serializers


class TeachersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teachers
        fields = '__all__'