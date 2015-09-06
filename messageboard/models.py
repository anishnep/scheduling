from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.


class Post(models.Model):
    posted_by=models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts")
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
   
    
    def __unicode__(self):
        return u'%s'%self.message
        
        
class Comment(models.Model):
    comment_by=models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments")
    post=models.ForeignKey(Post)
    comment_text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.comment_text
    
