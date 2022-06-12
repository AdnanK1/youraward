from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    image = CloudinaryField('image')
    link = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    likes = models.ManyToManyField(User,blank=True,related_name='likes')
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return str(self.user)

class Profile(models.Model):
    picture = CloudinaryField('picture')
    bio = models.TextField(max_length=60,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    contact = models.CharField(max_length=30)

    def __str__(self):
        return str(self.user)