from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'panda.views.index', name='home'),
    # url(r'^eureka/', include('eureka.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^hello/', 'panda.views.hello'),
    #url(r'^panda/bye/', 'panda.views.bye'),	
    url(r'^panda/', include('panda.urls')),
    #url(r'^rango/', include('rango.urls')),
    url(r'^signup/$','panda.views.contributer_signup'),
    url(r'^home/$','panda.views.home'),
    url(r'^logout/$', 'panda.views.user_logout', name='logout'),
    url(r'^comments/', include('django.contrib.comments.urls')),
	
)
if settings.DEBUG:
    urlpatterns += patterns('',
         (r'media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT})),

