from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Prescription, Patient
from myProject.serializers import PatientSerializer
from myApp.models import Patient

from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
# Create your views here.
def home(request):
    # Récupérer toutes les prescriptions depuis la base de données
    prescriptions = Prescription.objects.all()[:5]
    context = {'prescriptions': prescriptions,}
    # Passer les données à la template
    return render(request, 'myApp/index.html',context)

class PatientAPIView(APIView):
 
    def get(self, *args, **kwargs):
        categories = Patient.objects.all()
        serializer = PatientSerializer(categories, many=True)
        return Response(serializer.data)
    

class PatientViewset(ModelViewSet):
 
     serializer_class = PatientSerializer

     def get_queryset(self):
        return Patient.objects.all()
