from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    total_pacientes = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'nombre', 'especialidad', 'total_pacientes']

    def get_total_pacientes(self, obj):
        return obj.pacientes.count()