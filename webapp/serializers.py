from rest_framework import serializers
from .models import Employees


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('firstname', 'lastname')
        fields = '__all__'
