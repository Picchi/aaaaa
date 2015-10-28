from django.conf.urls import patterns, include, url
from django.conf import settings 
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
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^message/$',include('message.urls',namespace='message')),
	#url(r'^aste/',include('aste_core.urls',namespace='aste_core')),
	url(r'',include('aste_core.urls',namespace='aste_core')),

)
