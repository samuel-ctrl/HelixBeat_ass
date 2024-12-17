from rest_framework import generics
from .models import Patient, FamilyMember, Medication
from drf_spectacular.utils import extend_schema, extend_schema_view
from .serializers import (
    PatientSerializer,
    FamilyMemberSerializer,
    MedicationSerializer,
)


@extend_schema_view(
    get=extend_schema(tags=["Patients"]),
    post=extend_schema(tags=["Patients"]),
)
class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


@extend_schema_view(
    get=extend_schema(tags=["Patients"]),
    put=extend_schema(tags=["Patients"]),
    patch=extend_schema(tags=["Patients"]),
)
class PatientRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


@extend_schema_view(
    get=extend_schema(tags=["Family Members"]),
    post=extend_schema(tags=["Family Members"]),
)
class FamilyMemberListCreateView(generics.ListCreateAPIView):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer

    def get_queryset(self):
        return self.queryset.filter(patient_id=self.kwargs["patient_id"])


@extend_schema_view(
    get=extend_schema(tags=["Family Members"]),
    put=extend_schema(tags=["Family Members"]),
    patch=extend_schema(tags=["Family Members"]),
)
class FamilyMemberRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer


@extend_schema_view(
    get=extend_schema(tags=["Medications"]),
    post=extend_schema(tags=["Medications"]),
)
class MedicationListCreateView(generics.ListCreateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

    def get_queryset(self):
        return self.queryset.filter(
            patient_id=self.kwargs["patient_id"], is_active=True
        )


@extend_schema_view(
    get=extend_schema(tags=["Medications"]),
    put=extend_schema(tags=["Medications"]),
    patch=extend_schema(tags=["Medications"]),
)
class MedicationRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
