from django.contrib import admin
from .models import Report
# Register your models here.
class ReportAdmin(admin.ModelAdmin):
	class Meta:
		model = Report

admin.site.register(Report, ReportAdmin)