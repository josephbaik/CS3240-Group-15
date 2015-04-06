from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SecureWitness.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^reporterhome', 'SecureWitness.views.reporter', name='Home'),
    url(r'^adminhome', 'SecureWitness.views.adm', name='Home'),
    url(r'^readerhome', 'SecureWitness.views.reader', name='Home'),
<<<<<<< HEAD
    url(r'^SecWit/', include('SecWit.urls')),
=======
    url(r'^loginpage', 'SecureWitness.views.login', name='Login' )
>>>>>>> ca64e473c28af692262e041b7ff224207e7f6e81
)
