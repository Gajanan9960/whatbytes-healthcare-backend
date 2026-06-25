from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import PatientSerializer, DoctorSerializer, PatientDoctorMappingSerializer

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

class PatientDoctorMappingListCreateView(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

class PatientDoctorMappingDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        # Assignment: GET /api/mappings/<patient_id>/ - Get all doctors assigned to a specific patient
        mappings = PatientDoctorMapping.objects.filter(patient_id=pk)
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        # Assignment: DELETE /api/mappings/<id>/ - Remove a doctor from a patient
        mapping = get_object_or_404(PatientDoctorMapping, pk=pk)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

