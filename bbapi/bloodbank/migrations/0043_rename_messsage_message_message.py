# Generated by Django 3.2 on 2021-05-04 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0042_remove_patient_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='messsage',
            new_name='message',
        ),
    ]
