from rest_framework.serializers import ModelSerializer
 
from myApp.models import Patient
 
class PatientSerializer(ModelSerializer):
 
    class Meta:
        model = Patient
        fields = ['id', 'first_name','last_name', 'date_of_birth', ' address','phone_number']