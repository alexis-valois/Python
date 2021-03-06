#-*- coding: utf-8 -*-
from django.db import models

class Page(models.Model):                                                                               
    url = models.URLField()                                                                             
    nb_visites = models.IntegerField(default=1)                                                         
                                                                                                        
    def __unicode__(self):
        return self.url