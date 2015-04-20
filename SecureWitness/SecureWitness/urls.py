from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse

import login.views

urlpatterns = patterns('',
     #Examples:
     #url(r'^$', 'SecureWitness.views.home', name='home'),
     #url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'SecureWitness.views.firstscreen', name='homepage',),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reporterhome', 'SecureWitness.views.reporter', name='reporterHome'),
    url(r'^adminhome', 'SecureWitness.views.adm', name='adminHome'),
    url(r'^readerhome', 'SecureWitness.views.reader', name='Home'),
    url(r'^my_view/?$', 'SecureWitness.views.my_view', name='login-view',),
    url(r'^register/?$', 'SecureWitness.views.register', name='register',),
    url(r'^addUser/?$', 'SecureWitness.views.addUser', name='addUser',),
    url(r'^logout/?$', 'SecureWitness.views.logout_view', name = 'logout',),
    url(r'^requestforms/?$', 'SecureWitness.views.requestforms', name = 'requestforms',),
   
)
