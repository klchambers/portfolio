# Generated by Django 4.2.16 on 2025-01-09 18:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contactrequest_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactrequest',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]