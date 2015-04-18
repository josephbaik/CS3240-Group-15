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
    url(r'^reporterhome', 'SecureWitness.views.reporter', name='Home'),
    url(r'^adminhome', 'SecureWitness.views.adm', name='Home'),
    url(r'^readerhome', 'SecureWitness.views.reader', name='Home'),
    url(r'^my_view/?$', 'SecureWitness.views.my_view', name='login-view',),
    url(r'^register/?$', 'SecureWitness.views.register', name='register',),
    url(r'^addUser/?$', 'SecureWitness.views.addUser', name='addUser',),

)
