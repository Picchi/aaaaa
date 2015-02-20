from django.conf.urls import patterns, include, url
from aste_core import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aste.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$',views.index),
	url(r'(?P<str>.*)/',views.kk,name='kk'),
    
	

)
