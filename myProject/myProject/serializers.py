from rest_framework.serializers import ModelSerializer
 
from rest_framework import serializers
from myApp.models import Patient, Prescription

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'date_of_birth', 'address', 'phone_number')

class PrescriptionSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()  # Utilisation du sérialiseur Patient dans le sérialiseur Prescription

    class Meta:
        model = Prescription
        fields = ('patient', 'prescription_date', 'doctor_name', 'medication', 'instructions')
        
# Filtrer les prescriptions actives en utilisant .filter()
active_prescriptions = Prescription.objects.filter(is_active=True)

# Utilisez le sérialiseur PrescriptionSerializer pour sérialiser un queryset
prescriptions = Prescription.objects.all()  # Par exemple, vous pouvez obtenir toutes les prescriptions

serializer = PrescriptionSerializer(prescriptions, many=True)  # Utilisation de many=True pour renvoyer une liste

# Récupérez le résultat sous forme de liste avec la propriété .data
serialized_data = serializer.data

# Le résultat est maintenant une liste de prescriptions avec les détails des patients inclus.
