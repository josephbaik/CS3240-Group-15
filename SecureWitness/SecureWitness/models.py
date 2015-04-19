from django.db import models
from django.contrib.auth.models import User, Permission

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
    
    
    class Meta:
        permissions = (("add_page", "add page"), 
        ("read_page", "read page"), 
        ("manage_group", "manage group"),
        )