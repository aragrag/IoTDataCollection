# Generated by Django 4.2.6 on 2023-10-27 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iotapp', '0002_alter_iotobject_options_alter_iotobject_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iotobject',
            options={'verbose_name': 'Device IoT', 'verbose_name_plural': 'Devices IoT'},
        ),
    ]