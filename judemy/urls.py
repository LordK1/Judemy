from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'joins.views.home', name='home'),
                       url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='share'),
)
