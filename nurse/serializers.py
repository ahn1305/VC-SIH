# serializers.py
from rest_framework import serializers
from doctor.models import SalinePatientEntry

class SalinePatientEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SalinePatientEntry
        fields = '__all__'
