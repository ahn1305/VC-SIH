from django.contrib import admin
from .models import Patient


class PatientAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['id', 'patient_name', 'patient_age']

admin.site.register(Patient,PatientAdmin)