from django.contrib.auth.views import (
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls.base import reverse_lazy
from django.forms import Form

from users.forms.password import CustomPasswordResetForm



class CustomPasswordResetView(PasswordResetView):
    template_name:       str  = 'users/password/reset.html'
    email_template_name: str  = 'users/password/reset_email.html'
    form_class:          Form = CustomPasswordResetForm
    success_url               = reverse_lazy('user:password_reset_done')



class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name: str = 'users/password/reset_complete.html'



class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name: str = 'users/password/reset_confirm.html'
    success_url        = reverse_lazy('user:password_reset_complete')



class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name: str = 'users/password/reset_complete.html'
