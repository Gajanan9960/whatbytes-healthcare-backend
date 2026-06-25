from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PatientViewSet, 
    DoctorViewSet, 
    PatientDoctorMappingListCreateView, 
    PatientDoctorMappingDetailView
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'doctors', DoctorViewSet, basename='doctor')

urlpatterns = [
    path('mappings/', PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:pk>/', PatientDoctorMappingDetailView.as_view(), name='mapping-detail'),
    path('', include(router.urls)),
]
