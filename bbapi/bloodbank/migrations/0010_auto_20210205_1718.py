# Generated by Django 3.0.7 on 2021-02-05 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0009_auto_20210203_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='image',
            field=models.FileField(help_text='Attach your photo', upload_to=''),
        ),
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
