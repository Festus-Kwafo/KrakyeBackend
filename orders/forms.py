from django import forms
from .models import Order
from django_countries.data import COUNTRIES
from django.forms import ModelForm

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'country', 'location', 'phone_number')
