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
from django.http import JsonResponse

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # After saving the new entry, send JSON response with the latest entries
        latest_entries = SalinePatientEntry.objects.all().order_by('-inject_time')[:10]
        data = [{'prescribed_medicine': entry.prescribed_medicine,
                 'inject_time': entry.inject_time.strftime('%Y-%m-%d %H:%M:%S'),
                 'saline_ml': entry.saline_ml,
                 'patient_name': entry.patient_name,
                 'patient_room_number': entry.patient_room_number,
                 'patient_age': entry.patient_age,
                 'flow_rate_time': entry.flow_rate_time.strftime('%Y-%m-%d %H:%M:%S')} for entry in latest_entries]
        response_data = {'data': data}
        # You can return the JsonResponse here or use Django signals to notify the front-end
        return response_data
