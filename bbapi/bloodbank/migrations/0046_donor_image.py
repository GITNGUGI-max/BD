# Generated by Django 3.2 on 2021-05-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0045_donor_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='image',
            field=models.ImageField(default='default.png', help_text='Attach your photo', upload_to='upload/donor_images'),
        ),
    ]
