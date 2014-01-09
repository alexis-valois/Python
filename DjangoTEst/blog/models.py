#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    user = models.OneToOneField(User)  # La liaison OneToOne vers le modèle User
    site_web = models.URLField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    signature = models.TextField(null=True, blank=True)
    inscrit_newsletter = models.BooleanField(default=False)

    def __unicode__(self):
        return u"Profil de {0}".format(self.user.username)

class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to="photos/")

    def __unicode__(self):
           return self.nom

class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie')

    def __unicode__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que nous
        traiterons plus tard et dans l'administration
        """
        return u"%s" % self.titre

    class Meta:
        permissions = (
                ("commenter_article","Commenter un article"),
                ("marquer_article","Marquer un article comme lu"),
        )


class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nom


class Moteur(models.Model):
    nom = models.CharField(max_length=25)

    def __unicode__(self):
        return self.nom


class Voiture(models.Model):
    nom = models.CharField(max_length=25)
    moteur = models.OneToOneField(Moteur)

    def __unicode__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nom


class Vendeur(models.Model):
    nom = models.CharField(max_length=30)
    produits = models.ManyToManyField(Produit, through='Offre')

    def __unicode__(self):
        return self.nom


class Offre(models.Model):
    prix = models.IntegerField()
    produit = models.ForeignKey(Produit)
    vendeur = models.ForeignKey(Vendeur)
    def __unicode__(self):
        return "{0} vendu par {1}".format(self.produit, self.vendeur)