from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from approval.models import Approval
from approval.signals import request_approved
from django.core.mail import send_mail




class Employer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null = True,)
    company_name = models.CharField(max_length=120, default="<<add your company name>>")

    def __str__(self):
        return self.company_name


class Employee(models.Model):
    employer = models.ForeignKey(Employer, default=1)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank= True, null=True)
    emp_id = models.IntegerField(verbose_name='Employee-ID', unique=False)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=70, null = True, blank=True)
    has_got_password = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)

    class Meta:
        unique_together = ('emp_id', 'employer')

    def __str__(self):
        return self.first_name
        
    def get_full_name(self):
        return "%s %s"%(self.first_name, self.last_name)


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

@receiver(post_save, sender=Employee)
def create_user(sender, **kwargs):
    employee=kwargs["instance"]
    User=get_user_model()
      
    if kwargs["created"]:
        #generate random password
        password = generate_user_password(User)
        username=generate_username(employee.emp_id,employee.employer)
        
        #create a new user object
        new_user=User(username=username, email=employee.email, password='mypassword')
        
        new_user.save()
        employee.user=new_user 
        employee.save()
    
    #if an employee has not got password yet then..
    if employee.has_got_password == False:
        #pwd = generate_user_password(User)
        pwd="mypassword"
        send_password = send_password_on_email(employee, pwd)
        
        if send_password: 
            employee.user.set_password(pwd)
            employee.has_got_password=True
            employee.user.email=employee.email
            employee.save()
            employee.user.save()
        
        
        
#remove user associated with employee when deleting an employee.
@receiver(post_delete, sender=Employee)
def remove_user(sender, **kwargs):
    employee=kwargs["instance"]
    if employee.user:
        employee.user.delete()
        
#A function to send password to the email(development server email) provided. 
def send_password_on_email(obj, password=None):
    if obj.email:
        subject = "Password for test app"
        message = "your password :%s \n Note: you can change your password on next login. \n Thank you."%password
        send_mail(subject, message, 'localhost@localhost.com', [obj.email])
        return True
    return False
    
def generate_user_password(UserObj):
    return UserObj.objects.make_random_password()
    
def generate_username(employee_id, employer):
    return "%s@%s"%(str(employee_id),employer.company_name.lower())