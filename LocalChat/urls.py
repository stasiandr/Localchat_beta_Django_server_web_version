from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from ServerScript.models import ChatPoint
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LocalChat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin', include(admin.site.urls)),
    url(r'^myadmin$', 'ServerScript.views.print_array'),
    #url(r'^(.+)', 'ServerScript.views.parse'),
	url(r'^$', 'ServerScript.views.map_with_points') 
)
