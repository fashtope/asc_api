from django.db import models
from accountant.models import Accountant
from bank_draft.models import BankDraft

from student.models import Student


class Transaction(models.Model):
    class Meta:
        db_table = 'Transaction'
    transaction_number = models.CharField(max_length=250)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, related_name='student')
    accountant = models.ForeignKey(Accountant, on_delete=models.DO_NOTHING, related_name='accountant')
    created_date = models.DateTimeField(auto_now=True)
    bank_draft = models.OneToOneField(BankDraft, on_delete=models.DO_NOTHING)
    