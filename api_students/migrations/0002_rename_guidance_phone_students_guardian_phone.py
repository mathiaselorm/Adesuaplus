# Generated by Django 4.2.10 on 2024-02-08 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='guidance_phone',
            new_name='guardian_phone',
        ),
    ]
