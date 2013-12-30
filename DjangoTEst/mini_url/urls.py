#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('mini_url.views',
    url(r'^$', 'liste', name='url_liste'),  # Une string vide indique la racine
    url(r'^nouveau/$', 'nouveau', name='url_nouveau'),
    url(r'^(?P<code>\w{6})/$', 'redirection', name='url_redirection'),  # (?P<code>\w{6}) capturera 6 caractères alphanumériques. 
)