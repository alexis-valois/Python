#-*- coding: utf-8 -*-
__author__ = 'Alexis'

from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import ListView
from blog.views import FAQView
from blog.models import Article

urlpatterns = patterns('blog.views',
    url(r'^$', ListView.as_view(model=Article,
                                context_object_name='derniers_articles',
                                template_name='blog/accueil.html')),
    url(r'^home/$', 'home'), # Accueil du blog
    url(r'^article/(?P<id_article>\d+)/$', 'view_article'), # Vue d'un article
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', 'list_articles'), # Vue des articles d'un mois précis
    url(r'^redirection/$', 'view_redirection'),
    url(r'^tp1$', 'tpl'),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', 'addition'),
    url(r'^mapage', 'mapage'),
    url(r'^$', 'accueil'),
    url(r'^article/(?P<id>\d+)-(?P<slug>.+)$', 'lire'),
    url(r'^contact/$', 'contact'),
    url(r'^nouveau-contact/$', 'nouveau_contact'),
    url(r'^edit/(?P<id>\d+)/$', 'edit_article'),
    url(r'^voir-contact/$', 'voir_contacts'),
    url(r'^faq/$', FAQView.as_view()),   # Nous demandons la vue correspondant à la classe FAQView créée précédemment
)
urlpatterns += staticfiles_urlpatterns()