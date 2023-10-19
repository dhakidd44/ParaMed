from rest_framework.serializers import ModelSerializer
 
from rest_framework import serializers
from myApp.models import Patient, Prescription

from rest_framework import serializers
from myApp.models import Patient, Prescription

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'date_of_birth', 'address', 'phone_number')

class PrescriptionSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Prescription
        fields = ('patient', 'prescription_date', 'doctor_name', 'medication', 'instructions')

# Filtrer les prescriptions actives en utilisant .filter()
active_prescriptions = Prescription.objects.filter(is_active=True)

# Utilisez le sérialiseur PrescriptionSerializer pour sérialiser les prescriptions actives
serializer = PrescriptionSerializer(active_prescriptions, many=True)

# Récupérez le résultat sous forme de liste avec la propriété .data
serialized_data = serializer.data

# Le résultat est maintenant une liste de prescriptions actives avec les détails des patients inclus.
