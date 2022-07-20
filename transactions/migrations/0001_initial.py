# Generated by Django 4.0.3 on 2022-06-23 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0003_studentaddition_delete_student_student'),
        ('bank_draft', '0001_initial'),
        ('accountant', '0002_remove_accountantaddition_dob_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_number', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('accountant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='accountant', to='accountant.accountant')),
                ('bank_draft', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='bank_draft.bankdraft')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='student', to='student.student')),
            ],
            options={
                'db_table': 'Transaction',
            },
        ),
    ]
