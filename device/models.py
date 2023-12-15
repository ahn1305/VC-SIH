from django.db import models
import uuid
class Device(models.Model):
    device_id = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.device_id
    