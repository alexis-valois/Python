#-*- coding: utf-8 -*-
from django.db import models

class Eleve(models.Model):
    nom = models.CharField(max_length=31)
    moyenne = models.IntegerField(default=10)

    def __unicode__(self):
        return u"Élève {0} ({1}/20 de moyenne)".format(self.nom, self.moyenne)


class Cours(models.Model):
    nom = models.CharField(max_length=31)
    eleves = models.ManyToManyField(Eleve)

    def __unicode__(self):
        return self.nom