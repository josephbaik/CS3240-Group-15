from django.db import models
# Create your models here.
class Report(models.Model):
	title = models.CharField(max_length=128)
	views = models.IntegerField(default=0)
	author = models.CharField(max_length=128)
	date = models.CharField(max_length=128)
	url = models.URLField(default='bruh')
	short = models.TextField(default='none')
	longd = models.TextField(default='none')

	def __str__(self):
		return self.title