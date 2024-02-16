from . models import Administrators
from rest_framework import serializers


class AdministratorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Administrators
        fields = '__all__'