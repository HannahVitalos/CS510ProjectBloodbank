# Generated by Django 4.1.7 on 2023-03-30 01:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBank',
            fields=[
                ('bloodbank_name', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('phone_num', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('donor_id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('blood_type', models.CharField(choices=[('A+', 'A Pos'), ('A-', 'A Neg'), ('B+', 'B Pos'), ('B-', 'B Neg'), ('O+', 'O Pos'), ('O-', 'O Neg'), ('AB+', 'Ab Pos'), ('AB-', 'Ab Neg')], max_length=3)),
                ('email', models.EmailField(max_length=254)),
                ('phone_num', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=45)),
                ('health_interview', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='OperatingHours',
            fields=[
                ('day', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('hours', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('blood_type', models.CharField(choices=[('A+', 'A Pos'), ('A-', 'A Neg'), ('B+', 'B Pos'), ('B-', 'B Neg'), ('O+', 'O Pos'), ('O-', 'O Neg'), ('AB+', 'Ab Pos'), ('AB-', 'Ab Neg')], max_length=3)),
                ('email', models.EmailField(max_length=254)),
                ('phone_num', models.CharField(max_length=45)),
                ('doctor_name', models.CharField(max_length=45)),
                ('medical_need', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('volunteer_id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('phone_num', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=45)),
                ('training', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('staff_id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('phone_num', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=45)),
                ('position', models.CharField(max_length=45)),
                ('hours', models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(60)])),
                ('salary', models.IntegerField(validators=[django.core.validators.MinValueValidator(15000), django.core.validators.MaxValueValidator(500000)])),
                ('bloodbank_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodbankApp.bloodbank')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodbankApp.staffmember')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('donation_id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('blood_type', models.CharField(choices=[('A+', 'A Pos'), ('A-', 'A Neg'), ('B+', 'B Pos'), ('B-', 'B Neg'), ('O+', 'O Pos'), ('O-', 'O Neg'), ('AB+', 'Ab Pos'), ('AB-', 'Ab Neg')], max_length=3)),
                ('date_received', models.DateTimeField()),
                ('donor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodbankApp.donor')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodbankApp.staffmember')),
                ('volunteer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodbankApp.volunteer')),
            ],
        ),
        migrations.AddField(
            model_name='bloodbank',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodbankApp.operatinghours'),
        ),
    ]
