from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.conf.urls.static import static

import login.views
from SecureWitness import settings
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
    url(r'^reports/', include('reportUpload.urls')),
    url(r'^my_view/?$', 'SecureWitness.views.my_view', name='login-view',),
    url(r'^register/?$', 'SecureWitness.views.register', name='register',),
    url(r'^addUser/?$', 'SecureWitness.views.addUser', name='addUser',),
    url(r'^logout/?$', 'SecureWitness.views.logout_view', name = 'logout',),
    url(r'^SharingPage/?$', 'SecureWitness.views.SharingPage', name = 'SharingPage',),
    url(r'^shareReport/?$', 'SecureWitness.views.shareReport', name = 'shareReport',),
    url(r'^requestgroups/?$', 'SecureWitness.views.requestgroups', name = 'requestgroups',),
    url(r'^requestreports/?$', 'SecureWitness.views.requestreports', name = 'requestreports',),
    url(r'^requestlogin/?$', 'SecureWitness.views.login_user', name = 'requestlogin',),
    url(r'^newGroupPage/?$', 'SecureWitness.views.newGroupPage', name = 'newGroupPage',),
    url(r'^createGroup/?$', 'SecureWitness.views.createGroup', name = 'createGroup',),
    url(r'^addUserToGroup/?$', 'SecureWitness.views.addUserToGroup', name = 'addUserToGroup',),
    url(r'^addUserToGroupPage/?$', 'SecureWitness.views.addUserToGroupPage', name = 'addUserToGroupPage',),
    url(r'^searchForReports/?$', 'SecureWitness.views.searchForReports', name = 'searchForReports',),
    url(r'^listGroupsAndUsers/?$', 'SecureWitness.views.listGroupsAndUsers', name = 'listGroupsAndUsers',),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

