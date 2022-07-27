from django.shortcuts import redirect, render
from .forms import AppointmentForm
from django.views import generic
from .models import Appointment
from backend.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def appointment(request):
    form = AppointmentForm(request.POST)

    if request.method == "POST":
        appointment = Appointment()
        if form.is_valid():
            appointment.name = request.POST.get("name")
            appointment.email = request.POST.get("email")
            appointment.phone_number = request.POST.get("phone_number")
            appointment.date = request.POST.get("date")
            appointment.note = request.POST.get("note")
            appointment.regular_outfit = request.POST.get("regular_outfit")
            appointment.ceremonial_event = request.POST.get("urban_outfit")
            appointment.urban_outfit = request.POST.get("urban_outfit")
            appointment = form.save(commit=False)
            print(appointment.date)
            appointment.save()

            # setup Email
            subject = 'Appointment Book '
            message = f'Hello, {appointment.name} \n\nYour Appoitment Schedule for {appointment.date} has be received Successfuly. \n\nThese are appointment Information \n\nRegular Outfit:  {appointment.regular_outfit} \n\nCeremonial Event: {appointment.ceremonial_event} \n\nUrban Outfit:  {appointment.urban_outfit}\n\nAppointment Notes: {appointment.note}'
            to_email = appointment.email
            send_mail(subject, message, EMAIL_HOST_USER, [to_email])
            return redirect('appointment:appointment')
        else:
            print(form.errors.as_data())
            return redirect('appointment:appointment')
    context = {
        'form': form
    }
    return render(request, 'appointment.html', context )