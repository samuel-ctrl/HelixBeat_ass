from django.urls import path
from .views import (
    PatientListCreateView,
    PatientRetrieveUpdateView,
    FamilyMemberListCreateView,
    FamilyMemberRetrieveUpdateView,
    MedicationListCreateView,
    MedicationRetrieveUpdateView,
)

urlpatterns = [
    path(
        "patients/",
        PatientListCreateView.as_view(),
        name="patient-list-create",
    ),
    path(
        "patients/<int:pk>/",
        PatientRetrieveUpdateView.as_view(),
        name="patient-retrieve-update",
    ),
    path(
        "patients/<int:patient_id>/family-members/",
        FamilyMemberListCreateView.as_view(),
        name="family-member-list-create",
    ),
    path(
        "family-members/<int:pk>/",
        FamilyMemberRetrieveUpdateView.as_view(),
        name="family-member-retrieve-update",
    ),
    path(
        "patients/<int:patient_id>/medications/",
        MedicationListCreateView.as_view(),
        name="medication-list-create",
    ),
    path(
        "medications/<int:pk>/",
        MedicationRetrieveUpdateView.as_view(),
        name="medication-retrieve-update",
    ),
]
