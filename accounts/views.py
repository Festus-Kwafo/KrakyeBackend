from django.contrib.auth import login, logout
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import send_mail
from django.contrib import messages
from backend.settings import EMAIL_HOST_USER

from orders.views import user_orders
from .forms import RegistrationForm, UserEditForm, UserLoginForm
from .models import UserBase
from .tokens import account_activation_token


@login_required
def dashboard(request):
    orders = user_orders(request)
    return render(request, 'account/user/dashboard.html', {'orders':orders})


def account_register(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = True
            user.save()
            # setup Email
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = registerForm.cleaned_data.get('email')
            send_mail(subject, message, EMAIL_HOST_USER, [to_email])
            
            return redirect('/account/login/?command=verification&email='+user.email)

    else:
        registerForm = RegistrationForm()

    return render(request, 'account/registration/register.html', {'form': registerForm})

def login(request):
    if request.method == "POST":
        email = request.POST['email'].lower()
        password = request.POST['password']


        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('store:home')
        else:
            messages.warning(request, 'Invalid login credentials')
            return redirect('accounts:login')

    return render(request, 'account/registration/login.html' )

def account_activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UserBase.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Congulatulations, Your Account is Activated.🤗")
        # auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('accounts:login')
    else:
        messages.error(request, "Invalid Activation Link. 😥")
        return redirect('accounts:register')

@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
            
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request,
                  'account/user/edit_details.html', {'user_form': user_form})

@login_required
def delete_user(request):
    user = UserBase.objects.get(username=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('accounts:delete_confirmation')

