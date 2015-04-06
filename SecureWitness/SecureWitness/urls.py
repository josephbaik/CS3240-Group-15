from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse

import login.views

urlpatterns = patterns('',
     #Examples:
     #url(r'^$', 'SecureWitness.views.home', name='home'),
     #url(r'^blog/', include('blog.urls')),
   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reporterhome', 'SecureWitness.views.reporter', name='Home'),
    url(r'^adminhome', 'SecureWitness.views.adm', name='Home'),
    url(r'^readerhome', 'SecureWitness.views.reader', name='Home'),
<<<<<<< HEAD
    url(r'^$', login.views.ListUserView.as_view(), name='user-list'),
    url(r'^new$', login.views.CreateUserView.as_view(), name='user-new',),
    url(r'^edit/(?P<pk>\d+)/$', login.views.UpdateUserView.as_view(), name='user-edit',),
    url(r'^delete/(?P<pk>\d+)/$', login.views.DeleteUserView.as_view(), name='user-delete',),
    url(r'^(?P<pk>\d+)/$', login.views.UserView.as_view(), name='user-view',),
   )


=======
    url(r'^loginpage', 'SecureWitness.views.login', name='Login' )
)
>>>>>>> ca64e473c28af692262e041b7ff224207e7f6e81
