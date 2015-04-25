from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
# Create your models here.
class Report(models.Model):
        title = models.CharField(max_length=128)
        views = models.IntegerField(default=0)
        author = models.CharField(max_length=128)
        date = models.CharField(max_length=128, default='none')
        time = models.CharField(max_length=128, default='none')
        url = models.URLField(default='bruh')
        short = models.TextField(default='none')
        longd = models.TextField(default='none')
        location = models.TextField(default='none')
        users = models.ManyToManyField(User, related_name='reports')
        groups = models.ManyToManyField(Group, related_name='reports')

        def __str__(self):
                return self.title
