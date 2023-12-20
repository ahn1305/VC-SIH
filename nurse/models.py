# from django.db import models

# class SalinePatientEntry(models.Model):
#     prescribed_medicine = models.CharField(max_length=200)
#     inject_time = models.DateTimeField(auto_now=False, auto_now_add=False)
#     saline_ml = models.FloatField()
#     patient_name = models.CharField(max_length=200)
#     patient_room_number = models.IntegerField()
#     patient_age = models.IntegerField()
#     flow_rate_time = models.DateTimeField(auto_now=False, auto_now_add=False)

#     def __str__(self):
#         return self.patient_name
    

from django.db import models

class SalinePatientEntry(models.Model):
    prescribed_medicine = models.CharField(max_length=200)
    inject_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    saline_ml = models.FloatField()
    patient_name = models.CharField(max_length=200)
    patient_room_number = models.IntegerField()
    patient_age = models.IntegerField()
    flow_rate_time = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.patient_name
