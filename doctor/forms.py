
from django import forms

from django.forms import ModelForm
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from .models import SalinePatientEntry

class SalinePatientEntryForm(forms.ModelForm):
    inject_time  = forms.DateTimeField(widget=DateTimePickerInput())
    flow_rate_time = forms.DateTimeField(widget=DateTimePickerInput())

    class Meta:
        model = SalinePatientEntry
        fields = '__all__'

    class Media:

        css = {
            'all': ('https://cdn.jsdelivr.net/npm/flatpickr@4.6.2/dist/flatpickr.min.css',),
        }
        js = (
            'https://code.jquery.com/jquery-3.6.4.min.js',
            'https://cdn.jsdelivr.net/npm/flatpickr@4.6.2/dist/flatpickr.min.js',
        )

