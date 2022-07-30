from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.template import loader

from libraries.sendgrid_service.sendgrid_service import send_email


class CustomPasswordResetForm(PasswordResetForm):
    # HACK: We're using django's reset forms but a different mailing service,
    #       therefore, we're overriding `send_mail` but keeping everything else
    #       unchanged. And so, we're left with this messy argument list for this
    #       function, until I figure out a better way around this. Until this
    #       changes, leave out the type annotations as well.
    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
    ):
        send_email(
            from_email=settings.FROM_EMAIL,
            to_email=to_email,
            html_content=loader.render_to_string(email_template_name, context),
            subject="Password Reset for Newsfeed-Portal",
        )
