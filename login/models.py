from django.db import models
from django.core.urlresolvers import reverse
from django import forms
# Create your models here.


class User(models.Model):
   
   username = models.CharField(max_length=255,)
   
   email = models.EmailField()
   
   password1 = models.CharField(max_length=255)
   password2 = models.CharField(max_length=255)
   
   
   
   def __str__(self):
   
      return ' '.join([self.username, self.email,])
      
      
   def get_absolute_url(self):

      return reverse('user-view', kwargs={'pk': self.id})