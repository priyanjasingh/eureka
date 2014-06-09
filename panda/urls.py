from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'panda.views.hello'),
    #url(r'^hello$', 'panda.views.hello'),
    #url(r'^blog$', 'panda.views.blog'),	
    #url(r'^blog/submit/$','panda.views.submit_post'),
    url(r'^login/$','panda.views.userlogin'),
    url(r'^user/upload/$','panda.views.upload'),
    url(r'^user/review/$','panda.views.review'),
	
)


