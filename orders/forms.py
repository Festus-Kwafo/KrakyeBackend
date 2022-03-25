from django import forms
from .models import Order
from django_countries.data import COUNTRIES


class OrderForm(forms.ModelForm):
    username = forms.CharField(
        label='Enter Username', min_length=4, max_length=50, help_text='Required')
    full_name = forms.CharField(
        label='Enter Fullname', min_length=4, max_length=50, help_text='Required')
    country = forms.ChoiceField(choices=sorted(COUNTRIES.items()))    
    location = forms.CharField(
        label='Enter Address', min_length=4, max_length=50, help_text='Required')
    phone_number = forms.CharField(max_length=100, help_text='Required', error_messages={
        'required': 'Sorry, you will need a Phone Number'})
    
    class Meta:
        model = Order
        fields = ('username', 'full_name', 'country', 'location', 'phone_number')
