# Generated by Django 3.0.7 on 2021-02-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0028_auto_20210207_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.CharField(default='', help_text='Enter an email address', max_length=200),
        ),
    ]
