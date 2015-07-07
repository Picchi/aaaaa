from django.conf.urls import patterns, include, url
from aste_core import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$',views.index),
	#url(r'^index$',views.index),
	url(r'^search',views.search,name='search'),
	url(r'^sell_object/$',views.sell_object,name='ll'),
	url(r'^item/(?P<pk>[0-9]+)',views.show_item,name='show'),
	url(r'(?P<str>.*)/',views.kk,name='kk'),
)
