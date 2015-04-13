from django.conf.urls import patterns, include, url
from django.contrib import admin
import homescreen.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SecureWitness2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^readerhome', 'homescreen.views.reader', name='Home1'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'homescreen.views.firstscreen', name='homepage',),
    url(r'^my_view/?$', 'homescreen.views.my_view', name='login-view',),
    url(r'^register/?$', 'homescreen.views.register', name='register',),
    url(r'^addUser/?$', 'homescreen.views.addUser', name='addUser',),
    
)
