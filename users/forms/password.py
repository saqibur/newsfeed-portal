from django.conf import settings
from django.contrib.auth.forms import (
    PasswordResetForm,
)
from django.template import loader

from libraries.sendgrid_service.sendgrid_service import send_email



class CustomPasswordResetForm(PasswordResetForm):
    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name = None
    ):
        send_email(
            from_email   = settings.FROM_EMAIL,
            to_email     = to_email,
            html_content = loader.render_to_string(email_template_name, context),
            subject      = "Password Reset for Newsfeed-Portal",
        )
