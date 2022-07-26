# Generated by Django 4.0.3 on 2022-06-23 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0003_studentaddition_delete_student_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'Bank',
            },
        ),
        migrations.CreateModel(
            name='BankDraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draft_number', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bank_draft.bank')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.student')),
            ],
            options={
                'db_table': 'Bank draft',
            },
        ),
    ]
