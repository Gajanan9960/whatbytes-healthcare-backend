from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'gender', 'phone', 'address', 'created_by']
        read_only_fields = ['created_by']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'email', 'phone']

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'assigned_at']
        read_only_fields = ['assigned_at']
