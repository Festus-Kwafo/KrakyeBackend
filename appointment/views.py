from django.shortcuts import redirect, render
from .forms import AppointmentForm
from django.views import generic
from .models import Appointment

def appointment(request):
    form = AppointmentForm(request.POST)

    if request.method == "POST":
        appointment = Appointment()
        if form.is_valid():
            appointment.name = request.POST.get("name")
            appointment.email = request.POST.get("email")
            appointment.phone_number = request.POST.get("phone_number")
            appointment.time_slot = request.POST.get("time_slot")
            appointment.note = request.POST.get("note")
            appointment = form.save(commit=False)
            print(appointment.time_slot)
            appointment.save()
            return redirect('appointment:appointment')
        else:
            print(form.errors.as_data())
            return redirect('appointment:appointment')
    context = {
        'form': form
    }
    return render(request, 'appointment.html', context )