from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from approval.models import Approval
from approval.signals import request_approved
from django.core.mail import send_mail
from employer.models import Employer, Employee

class Work(models.Model):
    employee = models.ForeignKey(Employee)
    work_date = models.DateField(unique=False)
    has_work = models.BooleanField(default=False)
    worker_position = models.CharField(max_length=50)
    start_time = models.CharField(max_length=120, blank=True)
    end_time = models.CharField(max_length=120, blank=True)
    notes = models.CharField(max_length=120, verbose_name='Note', blank=True, null=True)

    def __str__(self):
        return '%s %s %s >> %s' % (self.work_date.year, self.work_date.month, self.work_date.day, self.has_work)
        
class WorkPosition(models.Model):
   position_name=models.CharField(max_length=50)
   
   def __str__(self):
       return self.position_name
    
class WorkRequest(models.Model):
    STATUS=(
        (1,'pending'),
        (2,'accepted'),
        (3,'rejected'),
    )
    REQUEST_TYPE=(
        (1, 'work day'),
        (2, 'free day'),
    )
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="work_request")
    request_date = models.DateField()
    request_type = models.IntegerField(choices= REQUEST_TYPE, default=1)
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    checked = models.BooleanField(default=False)
    approved_by = models.CharField(max_length=50, blank=True, null= True)


    def __str__(self):
        return('%s requested for %s is %s'%(self.get_request_type_display(), self.request_date, self.get_status_display()))
    
    def accept(self):
        self.status = 2 #accepted
        self.checked = True
        self.save()
        
    def reject(self):
        self.status = 3 #rejected
        self.checked=True
        self.save()
        
@receiver(post_save, sender=WorkRequest)
def create_approval_object(sender, **kwargs):
    if kwargs['created']:
        request_id=kwargs.get('instance').id
        a=Approval(work_request_id=request_id, approved= None)
        a.save()

@receiver(request_approved)
def work_request_approved(sender, **kwargs):
    print(kwargs['status'])
    w= WorkRequest.objects.get(id = kwargs['work_request_id'])  #get workrequest object
    if kwargs['status']:
        w.accept() #set approved to true and status to accepted
        employee=w.requested_by.employee
        try:
            work_obj = Work.objects.get(employee = employee, work_date = w.request_date)
        except work_obj.DoesNotExist:
            work_obj = None
        if work_obj:
            if w.request_type == 1: #if request is for work day
                work_obj.has_work = True

            elif w.request_type == 2: #if request is for free day
                work_obj.has_work = False

            work_obj.save()
        else:
            w.reject()

