from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescription_date = models.DateField()
    doctor_name = models.CharField(max_length=100)
    medication = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return f"Prescription for {self.patient}"