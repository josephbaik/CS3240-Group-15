from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse

import login.views
import SecureWitness.views
import reportUpload.views

urlpatterns = patterns('',
	    # url(r'^get/(?P<report_id>\d+)$', 'SecureWitness.views.Reportview', name='Report'),
	    # url(r'^get)/$', 'SecureWitness.views.Reportview', name='Report'),
	url(r'^get/(?P<report_id>[\w.@+-]+)/$', 'reportUpload.views.seereport', name='Report'),
	url(r'^all/$', 'SecureWitness.views.reader', name='read'),
	url(r'^mine/$', 'reportUpload.views.seemine', name='myreports'),
)