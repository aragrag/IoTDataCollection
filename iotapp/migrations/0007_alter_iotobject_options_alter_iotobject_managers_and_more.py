# Generated by Django 4.2.6 on 2023-10-27 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('iotapp', '0006_iotdata_iotobject_delete_customuser_iotdata_object'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iotobject',
            options={'verbose_name': 'Objet IoT', 'verbose_name_plural': 'Objets IoT'},
        ),
        migrations.AlterModelManagers(
            name='iotobject',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='iotobject',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='iotobject',
            name='email',
        ),
        migrations.RemoveField(
            model_name='iotobject',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='iotobject',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='iotobject',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='iotobject',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='iotobject',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='iotobject',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='iotobject',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='iotobject',
            name='password',
        ),
        migrations.RemoveField(
            model_name='iotobject',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='iotobject',
            name='username',
        ),
        migrations.AddField(
            model_name='iotobject',
            name='auth_token',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authtoken.token'),
        ),
        migrations.AlterField(
            model_name='iotobject',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]