from django.contrib import admin
from .forms import SalinePatientEntryForm

from .models import (
   SalinePatientEntry 
)

class SalinePatientEntryAdmin(admin.ModelAdmin):
    form = SalinePatientEntryForm

admin.site.register(SalinePatientEntry, SalinePatientEntryAdmin)

