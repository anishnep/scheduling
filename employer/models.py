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