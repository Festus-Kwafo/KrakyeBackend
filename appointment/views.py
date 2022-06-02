from django.shortcuts import render
from .forms import EventForm
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.views import generic
from .models import Appointment
class CreateView(generic.edit.CreateView):
    model = Appointment
    fields = ['name', 'email', 'phone_number', 'time_slot', 'note']
    def get_form(self):
        form = super().get_form()
        form.fields['time_slot'].widget = DateTimePickerInput()
        return form
# Create your views here.
def appointment(request):
    forms = EventForm()
    context = {
        'forms': forms
    }
    return render(request, 'appointment.html', context )