from django.db import models
from django.core.urlresolvers import reverse
from django import forms

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):      #For Python 2, use __str__ on Python 3
        return self.title

class User(models.Model):
   
   username = models.CharField(max_length=255,)
   
   email = models.EmailField()
   
   password1 = models.CharField(max_length=255)
   password2 = models.CharField(max_length=255)
   
   
   
   def __str__(self):
   
      return ' '.join([self.username, self.email,])
      
      
   def get_absolute_url(self):

      return reverse('user-view', kwargs={'pk': self.id})