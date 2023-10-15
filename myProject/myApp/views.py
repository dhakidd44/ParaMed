from django.shortcuts import render
from .models import Prescription, Patient

# Create your views here.
def home(request):
    # Récupérer toutes les prescriptions depuis la base de données
    prescriptions = Prescription.objects.all()[:5]
    context = {'prescriptions': prescriptions,}
    # Passer les données à la template
    return render(request, 'myApp/index.html',context)