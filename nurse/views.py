from django.shortcuts import render
from doctor.models import SalinePatientEntry

def nurse_interface(request):
    patient_entry_obj = SalinePatientEntry.objects.all()
    context = {"obj":patient_entry_obj}
    return render(request, 'nurse/nurse_interface.html', context=context)