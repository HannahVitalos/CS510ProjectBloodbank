# Generated by Django 4.1.7 on 2023-03-31 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbankApp', '0007_alter_bloodbank_table_alter_donation_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='operatinghours',
            table='OperatingHours',
        ),
        migrations.AlterModelTable(
            name='staffmember',
            table='StaffMember',
        ),
    ]
