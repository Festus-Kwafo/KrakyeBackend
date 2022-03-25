from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):

    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', }))

    amount = forms.IntegerField(
        label='Amount', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'amount', 'id': 'form-amount', }))

    class Meta:
        model = Payment
        fields = ('email', 'amount', )
