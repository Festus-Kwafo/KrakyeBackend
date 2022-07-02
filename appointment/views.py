from django.shortcuts import render
from .forms import EventForm
from django.views import generic
from .models import Appointment

def appointment(request):
    forms = EventForm()
    context = {
        'forms': forms
    }
    return render(request, 'appointment.html', context )