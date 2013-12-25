#-*- coding: utf-8 -*-
__author__ = 'Alexis'

from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('mini_url.views',
    url(r'^home/$', 'home'),
    url(r'^raccourcir/$', 'raccourcir'),
    url(r'^redirection/(?P<code>[-A-Za-z0-9_]{10})/$', 'redirection'),
)
urlpatterns += staticfiles_urlpatterns()