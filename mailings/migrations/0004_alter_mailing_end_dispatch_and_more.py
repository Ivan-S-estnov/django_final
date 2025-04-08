# Generated by Django 5.2 on 2025-04-08 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0003_alter_mailing_options_mailing_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="end_dispatch",
            field=models.DateTimeField(
                blank=True, help_text="yyyy-mm-dd 00:00:00", null=True, verbose_name="Дата и время окончания отправки"
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="first_dispatch",
            field=models.DateTimeField(
                blank=True, help_text="yyyy-mm-dd 00:00:00", null=True, verbose_name="Дата и время первой отправки"
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                choices=[("CO", "Завершена"), ("CR", "Создана"), ("LA", "Запущена")],
                default="CR",
                max_length=20,
                verbose_name="Статус",
            ),
        ),
    ]
