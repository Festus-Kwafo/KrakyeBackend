from django import forms
from .models import Order
from django_countries.data import COUNTRIES
from address.forms import AddressField
from django.forms import ModelForm

class OrderForm(ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Fullname', 'id': 'inputName'}))
    
    country = forms.ChoiceField(choices=sorted(COUNTRIES.items()))
    
    address = AddressField()

    location = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Your Location',}
        ))
    phone_number = forms.CharField(max_length=100, error_messages={
        'required': 'Sorry, you will need a Phone Number'})
    
    
    class Meta:
        model = Order
        fields = ('full_name', 'country', 'location', 'phone_number', 'post_code', 'address')
