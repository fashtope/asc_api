from django.db import models
from account.models import User

class VicePrincipalManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.VICE_PRINCIPAL)

class VicePrincipal(User):
    objects = VicePrincipalManager()
    
    class Meta:
        proxy = True
        
        
    def __str__(self):
        return self.more.staff_number
        
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.VICE_PRINCIPAL
        return super().save(*args, **kwargs)
    
    
    @property
    def more(self):
        return self.viceprincipaladdition    
    
    
    
class viceprincipaladdition(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_number = models.CharField(max_length=15, null=True, unique=True)

    