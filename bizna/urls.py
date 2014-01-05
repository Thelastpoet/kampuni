from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name="index"),
    
    # Companies Urls
    url(r'^add_company/$', views.CompanyCreateView.as_view(), name="add-company"),
    url(r'^company_list/$', views.CompanyCreateView.as_view(), name="list-company"),
)
