from django.conf.urls import patterns, include, url
from aste_core import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$',views.index),
	#url(r'^index$',views.index),
	url(r'^search',views.search,name='search'),
	url(r'^account',views.account,name='account'),
	url(r'^offerte',views.offerte,name='offerte'),
	url(r'^sell_object/$',views.sell_object,name='ll'),
	url(r'^item/(?P<pk>[0-9]+)(?P<mess>.*)',views.show_item,name='show'),
	url(r'^bid',views.bid,name='bid'),
	url(r'^compra_subito',views.compra_subito,name='compra_subito'),
	url(r'(?P<str>.*)/',views.kk,name='kk'),
)
