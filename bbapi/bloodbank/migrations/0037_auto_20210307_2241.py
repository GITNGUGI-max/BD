# Generated by Django 3.1.7 on 2021-03-07 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0036_auto_20210307_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.BooleanField(),
        ),
    ]
