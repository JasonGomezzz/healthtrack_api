from rest_framework import serializers
from .models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    doctor_nombre = serializers.CharField(source='doctor.nombre', read_only=True)
    doctor_especialidad = serializers.CharField(source='doctor.especialidad', read_only=True)

    class Meta:
        model = Paciente
        fields = ['id', 'nombre', 'edad', 'diagnostico', 'doctor', 'doctor_nombre', 'doctor_especialidad']