from rest_framework import serializers
from .models import Patient, FamilyMember, Medication


class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = "__all__"


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    family_members = FamilyMemberSerializer(many=True, read_only=True)
    medications = MedicationSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = "__all__"
