from django.conf.urls import patterns, include, url
from aste_core import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$',views.index),
	url(r'^ll/$',views.ll,name='ll'),
	url(r'(?P<str>.*)/',views.kk,name='kk'),
 )
