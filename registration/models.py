from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from timetable.models import Employer
# Create your models here.

class MyUser(AbstractUser):
    is_employer = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
        
@receiver(post_save, sender=MyUser)
def create_employer_object(sender, **kwargs):
    user=kwargs['instance']
    if kwargs["created"]:
        if user.is_employer:
            employer = Employer(user=user)
            employer.save()