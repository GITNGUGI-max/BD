# Generated by Django 3.2 on 2021-05-04 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0039_patient_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='image',
            field=models.FileField(help_text='Attach your photo', upload_to=''),
        ),
    ]
