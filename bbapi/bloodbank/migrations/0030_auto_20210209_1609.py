# Generated by Django 3.0.7 on 2021-02-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0029_message_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
