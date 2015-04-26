from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse

import login.views
import SecureWitness.views

urlpatterns = patterns('',
     #Examples:
     #url(r'^$', 'SecureWitness.views.home', name='home'),
     #url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'SecureWitness.views.firstscreen', name='homepage',),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reporterhome', 'SecureWitness.views.reporter', name='reporterHome'),
    url(r'^adminhome', 'SecureWitness.views.adm', name='adminHome'),
    url(r'^readerhome', 'SecureWitness.views.reader', name='Home'),
    url(r'^reportview/$', 'SecureWitness.views.Reportview', name='Report'),
    url(r'^my_view/?$', 'SecureWitness.views.my_view', name='login-view',),
    url(r'^register/?$', 'SecureWitness.views.register', name='register',),
    url(r'^addUser/?$', 'SecureWitness.views.addUser', name='addUser',),
    url(r'^logout/?$', 'SecureWitness.views.logout_view', name = 'logout',),
    url(r'^requestgroups/?$', 'SecureWitness.views.requestgroups', name = 'requestgroups',),
    url(r'^requestreports/?$', 'SecureWitness.views.requestreports', name = 'requestreports',),
    url(r'^requestlogin/?$', 'SecureWitness.views.login_user', name = 'requestlogin',),
    url(r'^newGroupPage/?$', 'SecureWitness.views.newGroupPage', name = 'newGroupPage',),
    url(r'^createGroup/?$', 'SecureWitness.views.createGroup', name = 'createGroup',),
    url(r'^addUserToGroup/?$', 'SecureWitness.views.addUserToGroup', name = 'addUserToGroup',),
    url(r'^addUserToGroupPage/?$', 'SecureWitness.views.addUserToGroupPage', name = 'addUserToGroupPage',),

    # url(r'^reportview/(?P<report>\w+)/$', 'app.views.Reportview', name='report'),
)
