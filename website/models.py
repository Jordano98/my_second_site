from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255,blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  

    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email=models.EmailField()

    def __str__(self):
        return self.email



class Team(User):
    position=models.CharField(max_length=255)
    image= models.ImageField(upload_to='website/', default='./team-1.jpg')

    class Meta:
        verbose_name='team member'
# Create your models here.
