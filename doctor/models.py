from django.db import models
from patient.models import Patient
from device.models import Device

class SalinePatientEntry(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    prescribed_medicine = models.CharField(max_length=200)
    inject_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    saline_ml = models.FloatField()
    flow_rate_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.patient.patient_name} - {self.prescribed_medicine}"
    
