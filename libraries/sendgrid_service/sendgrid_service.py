from os import environ

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

_SEND_GRID_API_CLIENT: SendGridAPIClient = SendGridAPIClient(environ.get('SENDGRID'))


def send_email(
    from_email:   str,
    to_email:     str,
    subject:      str,
    html_content: str,
):
    try:
        _SEND_GRID_API_CLIENT.send(Mail(
            from_email   = from_email,
            to_emails    = to_email,
            subject      = subject,
            html_content = html_content,
        ))
    except Exception as exn:
        raise exn
