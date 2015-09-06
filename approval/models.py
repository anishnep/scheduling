from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from .signals import request_approved

# Create your models here.
class Approval(models.Model):
    work_request_id = models.PositiveIntegerField()
    approved = models.NullBooleanField()

    def save(self,**kwargs):
        if self.pk is not None and self.approved is not None:
            request_approved.send(self, work_request_id=self.work_request_id, status=self.approved)

        super(Approval, self).save(kwargs)
    def __str__(self):
        return "%s id is waiting for approval"%self.work_request_id
    
@receiver(post_save, sender = Approval)
def remove_approval_object(sender, **kwargs):
    if not kwargs['created']:
        approval = kwargs['instance'] #approval object instance being saved
        if approval.approved is not None:
            approval.delete() #delete object instance
            
            