#-*- coding: utf-8 -*-
__author__ = 'Alexis'
#-*- coding: utf-8 -*-
from models import Page #Nous importons le modèle défini précédemment


class StatsMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):  # À chaque appel de vue
        try:
            p = Page.objects.get(url=request.path)  # Le compteur lié à la page est récupéré
            p.nb_visites += 1
            p.save()
        except Page.DoesNotExist:  # Si la page n'a pas encore été consultée
            Page(url=request.path).save()  # Un nouveau compteur à 1 par défaut est créé

    def process_response(self, request, response):  # À chaque réponse
        if response.status_code == 200:
            p = Page.objects.get(url=request.path)
            response.content += "Cette page à été vue {0} fois.".format(p.nb_visites)
        return response