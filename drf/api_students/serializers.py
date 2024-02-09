from . models import students
from rest_framework import serializers



class studentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'