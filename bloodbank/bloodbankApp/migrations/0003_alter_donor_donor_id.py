# Generated by Django 4.1.7 on 2023-03-30 17:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbankApp', '0002_rename_donor_id_donation_donor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='donor_id',
            field=models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]