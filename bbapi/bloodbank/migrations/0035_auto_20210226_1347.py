# Generated by Django 3.0.7 on 2021-02-26 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0034_auto_20210219_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='image',
            field=models.FileField(default='default.jpg', upload_to='profile_pic'),
        ),
        migrations.AddField(
            model_name='patient',
            name='image',
            field=models.FileField(default='default.jpg', upload_to='profile_pic'),
        ),
    ]
