from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views
from .forms import (UserLoginForm, PwdResetForm, PwdResetConfirmForm)

app_name = 'accounts'

urlpatterns = [
     path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.account_register, name='register'),
    #activate account
    path('activate/<slug:uidb64>/<slug:token>)/', views.account_activate, name='activate'),
    
    # reset password
    path('password_reset/', views.passwordforgot, name='pwdreset'),
    path('password_reset_validate/<uidb64>/<token>', views.pwdresetvalidate, name="password_reset_confirm"),
    path('password_reset/password_reset_email_confirm/', views.resetPassword,  name='resetPassword'),
    path('password_reset_confirm/<slug:uidb64>/password_reset_complete/',
         TemplateView.as_view(template_name="account/user/reset_status.html"), name='password_reset_complete'),
    # user dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('my_orders', views.my_orders, name='my_orders'),
    path('profile/edit', views.edit_details, name='edit_details'),
    path('profile/delete_user', views.delete_user, name='delete_user'),
    path('profile/delete_confirm',TemplateView.as_view(template_name='account/user/delete_confirmation.html'), name='delete_confirmation'),

]
