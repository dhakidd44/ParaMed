from rest_framework.serializers import ModelSerializer
from rest_framework.test import APITestCase
from rest_framework import serializers
from myApp.models import Patient, Prescription
from django.urls import reverse
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

# Creation d un test
serialized_data = serializer.data
class PatientDetailAPITest(APITestCase):
    def setUp(self):
        # Créez un patient de test
        self.patient = Patient.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth="1990-01-01",
            address="123 Main St",
            phone_number="123-456-7890"
        )

    def test_get_patient_detail(self):
        # Créez l'URL pour le détail du patient en utilisant reverse
        url_detail = reverse('patient-detail', kwargs={'pk': self.patient.pk})

        # Effectuez une requête GET vers l'URL de détail
        response = self.client.get(url_detail)

        # Vérifiez que le statut de la réponse est 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Créez le dictionnaire des données attendues au format spécifique
        expected = {
            'id': self.patient.pk,
            'first_name': self.patient.first_name,
            'last_name': self.patient.last_name,
            'date_of_birth': self.patient.date_of_birth.strftime('%Y-%m-%d'),
            'address': self.patient.address,
            'phone_number': self.patient.phone_number,
        }

        # Vérifiez que les données sérialisées correspondent aux données attendues
        self.assertEqual(expected, response.data)
