from django import forms
from .models import Appointment

class EventForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone_number', 'time_slot', 'note']