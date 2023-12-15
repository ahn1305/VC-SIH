from django.db import models
import uuid

class Patient(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_room_number = models.IntegerField()
    patient_age = models.IntegerField()


    def __str__(self):
        return self.patient_name