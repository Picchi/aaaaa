from django.conf.urls import patterns, include, url
#from aste import views
from aste import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page),
    url(r'^sign_up/$', views.sign_up_page),
	#url(r'^aste/',include('aste_core.urls',namespace='aste_core')),
	url(r'',include('aste_core.urls',namespace='aste_core')),

)
