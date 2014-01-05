from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('bizna.urls', namespace="bizna")),
    
    # User Authentication
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
     {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls', namespace='accounts')), 
       
)
