# Generated by Django 3.0.7 on 2021-02-02 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0008_auto_20200721_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='subCounty',
            field=models.ForeignKey(help_text='Enter your county of residence', on_delete=django.db.models.deletion.CASCADE, to='bloodbank.SubCounty'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='subCounty',
            field=models.ForeignKey(help_text='Enter your county of residence', on_delete=django.db.models.deletion.CASCADE, to='bloodbank.SubCounty'),
        ),
    ]
