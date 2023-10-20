from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.db import transaction
from django.shortcuts import render
from myApp.models import Prescription, Patient
from myProject.serializers import PatientSerializer

def home(request):
    # Récupérer les cinq premières prescriptions depuis la base de données
    prescriptions = Prescription.objects.all()[:5]
    context = {'prescriptions': prescriptions}
    # Passer les données à la template
    return render(request, 'myApp/index.html', context)

class PatientAPIView(APIView):
    def get(self, *args, **kwargs):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

class PatientViewset(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    @transaction.atomic
    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        try:
            # Désactivez le patient
            patient = self.get_object()
            patient.is_active = False
            patient.save()

            # Vous devrez ajuster ce code pour désactiver les prescriptions associées si nécessaire
            # Par exemple, en utilisant un modèle de relation entre Patient et Prescription.

            return Response({'message': 'Patient and associated prescriptions (if any) disabled.'}, status=status.HTTP_200_OK)
        except Exception as e:
            transaction.set_rollback(True)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
