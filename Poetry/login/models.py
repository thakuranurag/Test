from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user_data(models.Model):
    fcm = models.CharField(max_length=240, blank=False, null=False)
    first_name= models.CharField(max_length=240, blank=False, null=False)
    second_name=models.CharField(max_length=240, blank=False, null=False)
    mobile = models.CharField(max_length=16, blank=False, null=False)
    image = models.ImageField(upload_to='profile/')
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    email = models.CharField(max_length=150, blank=True, null = True)

    def __unicode__(self):
        return self.email



class otp_data(models.Model):

    otp = models.IntegerField(default=0)
    flag = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    email = models.CharField(max_length=150, blank=True, null = True)
