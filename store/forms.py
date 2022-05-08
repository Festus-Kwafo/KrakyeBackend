from random import choices
from django import forms

COLOR_CHOICES = (
        ('R', 'Red'),
    ('B', 'Blue')
)
    

class ProductForm(forms.Form):
    color = forms.ChoiceField(choices=COLOR_CHOICES)
    size = forms.ChoiceField()