from django.db import models

from student.models import Student
from accountant.models import Accountant

class Fees(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.IntegerField()
    reference = models.CharField(max_length=255)
    # accountant = models.ForeignKey(Accountant, on_delete=models.DO_NOTHING, null=True, blank=False)
    date = models.DateField(auto_now=True)
 