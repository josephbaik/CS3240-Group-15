from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core import urlresolvers
# Create your models here.

class Folder(models.Model):
        root = models.ForeignKey('self', null=True)
        user = models.ForeignKey(User)
        name = models.CharField(max_length=200)

class Report(models.Model):
        title = models.CharField(max_length=128)
        views = models.IntegerField(default=0)
        author = models.CharField(max_length=128)
        date = models.CharField(max_length=128, default='')
        time = models.CharField(max_length=128, default='')
        url = models.URLField(default='')
        short = models.TextField(default='')
        longd = models.TextField(default='')
        location = models.TextField(default='')
        users = models.ManyToManyField(User, related_name='reports')
        groups = models.ManyToManyField(Group, related_name='reports')
        tags = models.TextField(default='')
        reportID = models.TextField(default='0000')
        enckey = models.CharField(max_length=516, default='')
        folder = models.TextField(max_length=516, default='')
        
        def get_absolute_url(self):
                return urlresolvers.reverse('report', args=(self.title,))

        def __str__(self):
                return self.title
