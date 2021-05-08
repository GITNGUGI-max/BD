# Generated by Django 3.2 on 2021-05-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0046_donor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='image',
            field=models.FileField(default='default.png', help_text='Attach your photo', upload_to='upload/donor_images'),
        ),
    ]