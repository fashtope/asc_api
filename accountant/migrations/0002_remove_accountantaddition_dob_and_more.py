# Generated by Django 4.0.3 on 2022-06-23 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountantaddition',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='accountantaddition',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='accountantaddition',
            name='othername',
        ),
        migrations.RemoveField(
            model_name='accountantaddition',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='accountantaddition',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='accountantaddition',
            name='updated_at',
        ),
    ]
