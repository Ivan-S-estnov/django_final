from django.utils import timezone
from config.settings import EMAIL_HOST_USER
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from mailings.models import Mailing, MailingAttempt


def send_mailing(mailing):
    recipients = mailing.recipients.all()
    for recipient in recipients:
        try:
            send_mail(
                mailing.message.subject,
                mailing.message.body,
                EMAIL_HOST_USER,
                [recipient.email],
            )
            MailingAttempt.objects.create(
                date_attempt=timezone.now(),
                status='SU',
                mail_response='Сообщение отправлено',
                mailing=mailing,
            )
            print(
                f'Сообщение {mailing.message.subject} успешно отправлено на почту {recipient.email}'
            )
        except Exception as e:
            MailingAttempt.objects.create(
                date_attempt=timezone.now(),
                status='FA',
                mail_response=str(e),
                mailing=mailing,
            )
            print(str(e))


class Command(BaseCommand):
    help = 'Send messages'

    def handle(self, *args, **kwargs):
        messages = Mailing.objects.filter(status__in=['CR', 'LA'])
        for mailing in messages:
            send_mailing(mailing)