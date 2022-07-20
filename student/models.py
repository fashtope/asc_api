from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from account.models import User
# Create your models here.

class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.STUDENT)

class Student(User):
    objects = StudentManager()
    
    class Meta:
        proxy = True
        
        
    def __str__(self):
        return self.more.index_number
        
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.STUDENT
        return super().save(*args, **kwargs)
    
    
    @property
    def more(self):
        return self.studentaddition    
    
    
    
class StudentAddition(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    index_number = models.CharField(max_length=15, null=True, unique=True)
    
    
