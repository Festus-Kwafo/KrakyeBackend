from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)
from requests import request

from .models import UserBase
from django.contrib import auth

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'johndoe@sample.com', 'id': 'inputEmail'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'inputPassword',
        }
    ))
    
    def clean(self):
        username = self.cleaned_data.get('username').lower()
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = auth.authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
    
        


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        label='Enter Username', min_length=4, max_length=50, help_text='Required', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username',}))
    first_name = forms.CharField(
        label='Enter Firstname', min_length=3, max_length=50, help_text='Required', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'John',}))
    last_name = forms.CharField(
        label='Enter Last name', min_length=3, max_length=50, help_text='Required', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Doe',}))
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required': 'Sorry, you will need an email', })
    phone_number = forms.CharField(max_length=14, help_text='Required', error_messages={
        'required': 'Sorry, you will need a Phone Number'}, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '+2335547982365',}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = UserBase.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'johndoe1'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'johndoe@sample.com', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': ''})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': ''})


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))
    first_name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Firstname', 'id': 'form-firstname'}))
    last_name = forms.CharField(
        label='Lastname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Lastname', 'id': 'form-lastname'}))
    phone_number = forms.CharField(
        label='Phone Number', min_length=4, max_length=14, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Phone Number', 'id': 'form-phonenumber'}))
    address_line_1 = forms.CharField(
        label='Address Line 1', widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Address Line 1', 'id': 'form-adressline1'}))
    address_line_2 = forms.CharField(
        label='Address Line 2', widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Address Line 2', 'id': 'form-adressline2'}))
    country = forms.CharField(
        label='Address Line 2', widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Country', 'id': 'form-adressline2'}))
    state = forms.CharField(
        label='Address Line 2', widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'State/Region', 'id': 'form-adressline2'}))
    city = forms.CharField(
        label='Address Line 2', widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'City', 'id': 'form-adressline2'}))
    profile_picture = forms.CharField(
        label='Phone Number', widget=forms.FileInput(
            attrs={'class': 'form-control', 'placeholder': 'Phone Number', 'id': 'form-profilepicture'}))

    class Meta:
        model = UserBase
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'address_line_1', 'address_line_2', 'profile_picture')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['phone_number'].required = True
        self.fields['address_line_1'].required = True
        self.fields['address_line_2'].required = True
        self.fields['profile_picture'].required = False
        self.fields['email'].required = True


class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = UserBase.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Unfortunatley we can not find that email address')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))
    