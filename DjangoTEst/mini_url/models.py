#-*- coding: utf-8 -*-
from django.db import models


class MiniURL(models.Model):
    longURL = models.URLField(unique=True, null=False, verbose_name="Longue URL")
    code = models.CharField(unique=True, max_length=2083, verbose_name="Code d'URL")
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    pseudo = models.CharField(null=False, max_length=255, verbose_name="Pseudo")
    nbAcces = models.IntegerField(default=0, verbose_name="Nombre d'accès à l'URL")

    def __unicode__(self):
        return self.longURL