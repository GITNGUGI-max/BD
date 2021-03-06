# Generated by Django 3.0.8 on 2020-07-06 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.IntegerField(help_text='Enter count number', primary_key=True, serialize=False)),
                ('countyName', models.TextField(help_text='Enter county name')),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donorName', models.CharField(help_text='Enter donor name', max_length=250)),
                ('parentName', models.CharField(help_text='enter parent or guardian name', max_length=250)),
                ('gender', models.CharField(help_text='Enter your sex', max_length=100)),
                ('dateOfBirth', models.DateField(verbose_name='Date of Birth')),
                ('bloodGroup', models.CharField(help_text='Enter your blood type', max_length=10)),
                ('weight', models.IntegerField(help_text='enter weight in KGs')),
                ('email', models.CharField(help_text='Enter an email address', max_length=200)),
                ('location', models.CharField(help_text='Enter your current location', max_length=200)),
                ('contactOne', models.IntegerField(help_text='Enter your contact number')),
                ('contactTwo', models.IntegerField(help_text='Enter your contact number')),
                ('voluntary', models.TextField(default='Yes', max_length=10)),
                ('newDonor', models.CharField(default='Yes', max_length=10)),
                ('lastDonated', models.DateField(null=True)),
                ('image', models.ImageField(help_text='Attach your photo', upload_to='')),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'Inactive')], default=0, help_text='DONOR STATUS', max_length=10)),
                ('county', models.ForeignKey(help_text='Enter your county of residence', on_delete=django.db.models.deletion.CASCADE, to='bloodbank.County')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientName', models.CharField(help_text='Enter patient name', max_length=250)),
                ('hospital', models.CharField(help_text='Enter hospital name', max_length=250)),
                ('doctor', models.CharField(help_text='Enter your doctors name', max_length=100)),
                ('contactName', models.CharField(help_text='Enter your contact name', max_length=100)),
                ('email', models.CharField(help_text='Enter an email address', max_length=200)),
                ('contactDate', models.DateField(auto_now_add=True)),
                ('requiredDate', models.DateField(auto_now_add=True)),
                ('bloodUnits', models.IntegerField(help_text='Enter amount of blood required')),
                ('bloodGroup', models.CharField(help_text='Enter your blood type', max_length=10)),
                ('contactOne', models.IntegerField(help_text='Enter your contact number')),
                ('contactTwo', models.IntegerField(help_text='Enter your contact number')),
                ('reason', models.TextField(help_text='Enter reason for requiring blood')),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'Inactive')], default=0, help_text='PANICIENT STATUS', max_length=10)),
                ('image', models.ImageField(help_text='Attach your photo', upload_to='')),
                ('county', models.ForeignKey(help_text='Enter your county of residence', on_delete=django.db.models.deletion.CASCADE, to='bloodbank.County')),
            ],
        ),
        migrations.CreateModel(
            name='subCounty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCountyName', models.TextField(help_text='Enter county name')),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodbank.County')),
            ],
        ),
        migrations.CreateModel(
            name='PatientMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.IntegerField(help_text='Enter your contact number')),
                ('email', models.CharField(help_text='Enter an email address', max_length=200)),
                ('Date', models.DateField(auto_now_add=True)),
                ('messsage', models.TextField(help_text='Write your message')),
                ('status', models.CharField(choices=[('r', 'Read'), ('un', 'Unread')], default=0, help_text='MESSAGE_STATUS', max_length=10)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodbank.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='subCounty',
            field=models.ForeignKey(help_text='Enter your county of residence', on_delete=django.db.models.deletion.CASCADE, to='bloodbank.subCounty'),
        ),
        migrations.CreateModel(
            name='DonorMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.IntegerField(help_text='Enter your contact number')),
                ('email', models.CharField(help_text='Enter an email address', max_length=200)),
                ('Date', models.DateField(auto_now_add=True)),
                ('messsage', models.TextField(help_text='Write your message')),
                ('status', models.CharField(choices=[('r', 'Read'), ('un', 'Unread')], default=0, help_text='MESSAGE_STATUS', max_length=10)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodbank.Donor')),
            ],
        ),
        migrations.AddField(
            model_name='donor',
            name='subCounty',
            field=models.ForeignKey(help_text='Enter your county of residence', on_delete=django.db.models.deletion.CASCADE, to='bloodbank.subCounty'),
        ),
    ]
