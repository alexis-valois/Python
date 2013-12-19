#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from datetime import datetime
from blog.models import Article, Contact
from blog.forms import ContactForm, ArticleForm, NouveauContactForm


def contact(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ContactForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']

            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer

            envoi = True

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ContactForm()  # Nous créons un formulaire vide

    return render(request, 'blog/contact.html', locals())


def edit_article(request, id):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        article = get_object_or_404(Article, id=id)
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
        return redirect('blog.views.edit_article', id)
    else:
        article = get_object_or_404(Article, id=id)
        article_form = ArticleForm(instance=article)
        return render(request, 'blog/edit_article.html', {'article_form': article_form, 'id': id})


def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles':articles})


def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article':article})


def home(request):
    text = """<h1>Bienvenue sur mon blog !</h1>
            <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)


def view_article(request, id_article):
    """ Vue qui affiche un article selon son identifiant (ou ID, ici un numéro). Son ID est le second paramètre de la fonction
        (pour rappel, le premier paramètre est TOUJOURS la requête de l'utilisateur) """
    if int(id_article) > 100: #Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
        raise Http404

    if not id_article == 42:
        return redirect('blog.views.view_article', id_article=42)


def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")


def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """

    text = "Vous avez demandé les articles de {0} {1}.".format(month, year)
    return HttpResponse(text)


def tpl(request):
    return render(request, 'blog/tpl.html', {'current_date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)
    # retourne nombre1, nombre2 et la somme des deux
    return render(request, 'blog/addition.html', locals())


def mapage(request):
    return render(request, 'blog/mapage.html')


def nouveau_contact(request):
    sauvegarde = False

    if request.method == "POST":
           form = NouveauContactForm(request.POST, request.FILES)
           if form.is_valid():
                   contact = Contact()
                   contact.nom = form.cleaned_data["nom"]
                   contact.adresse = form.cleaned_data["adresse"]
                   contact.photo = form.cleaned_data["photo"]
                   contact.save()

                   sauvegarde = True
    else:
           form = NouveauContactForm()

    return render(request, 'blog/contact.html',locals())