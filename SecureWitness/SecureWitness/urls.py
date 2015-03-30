from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'SecureWitness.views.index', name='Home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^admin/', include(admin.site.urls)),

)
