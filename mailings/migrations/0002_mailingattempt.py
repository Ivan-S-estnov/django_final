# Generated by Django 5.2 on 2025-04-05 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MailingAttempt",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "date_attempt",
                    models.DateTimeField(help_text="yyyy-mm-dd 00:00:00", verbose_name="Дата и время попытки"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("SU", "Успешно"), ("FA", "Не успешно")], max_length=20, verbose_name="Статус"
                    ),
                ),
                ("mail_response", models.TextField(verbose_name="Ответ почтового сервера")),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mailing_attempts",
                        to="mailings.mailing",
                        verbose_name="Рассылка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Попытка",
                "verbose_name_plural": "Попытки",
                "ordering": ["status", "date_attempt"],
            },
        ),
    ]
