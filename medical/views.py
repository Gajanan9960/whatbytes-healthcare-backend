from rest_framework import viewsets, permissions, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
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

class PatientDoctorMappingViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = PatientDoctorMapping.objects.all()

    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='(?P<patient_id>[^/.]+)')
    def get_doctors_for_patient(self, request, patient_id=None):
        mappings = self.get_queryset().filter(patient_id=patient_id)
        serializer = self.get_serializer(mappings, many=True)
        return Response(serializer.data)
