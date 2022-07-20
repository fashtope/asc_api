from django.db import models

from student.models import Student


class Bank(models.Model):
    class Meta:
        db_table = 'Bank'
    name = models.CharField(max_length=255, unique=True)

class BankDraft(models.Model):
    class Meta:
        db_table = 'Bank draft'
        
    bank = models.ForeignKey(Bank, on_delete=models.DO_NOTHING)
    draft_number = models.CharField(max_length=255)
    amount = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)