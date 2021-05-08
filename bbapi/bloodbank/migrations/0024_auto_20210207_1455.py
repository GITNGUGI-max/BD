# Generated by Django 3.0.7 on 2021-02-07 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0023_auto_20210207_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('r', 'Read'), ('un', 'Unread')], default='un', help_text='MESSAGE_STATUS', max_length=10),
        ),
    ]