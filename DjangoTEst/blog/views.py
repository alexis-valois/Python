#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from datetime import datetime
from blog.models import Article, Contact, Categorie
from blog.forms import ContactForm, ArticleForm, NouveauContactForm
from django.contrib import messages
from blog.forms import ContactForm, ArticleForm, NouveauContactForm, ConnexionForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render
from django.core.urlresolvers import reverse


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]  # Nous récupérons le nom d'utilisateur
            password = form.cleaned_data["password"]  # … et le mot de passe
            user = authenticate(username=username, password=password)  #Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: #sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'blog/connexion.html',locals())


class LireArticle(DetailView):
    context_object_name = "article"
    model = Article
    template_name = "blog/lire.html"


class FAQView(TemplateView):
    template_name = "blog/faq.html"


class ListeArticles(ListView):
    model = Article
    context_object_name = "derniers_articles"
    template_name = "blog/accueil.html"
    paginate_by = 5

    def get_queryset(self):
       return Article.objects.filter(categorie__id=self.args[0])

    def get_context_data(self, **kwargs):
       # Nous récupérons le contexte depuis la super-classe
       context = super(ListeArticles, self).get_context_data(**kwargs)
       # Nous ajoutons la liste des catégories, sans filtre particulier
       context['categories'] = Categorie.objects.all()
       return context


def accueil(request):
    messages.add_message(request, messages.INFO, u'Bonjour visiteur !')
    return render(request, 'blog/accueil.html')


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


#def lire(request, id, slug):
#    article = get_object_or_404(Article, id=id, slug=slug)
#    return render(request, 'blog/lire.html', {'article':article})


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


def citation(request):
    return render(request, 'blog/citation.html')


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

    return render(request, 'blog/contact.html', locals())


def voir_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'blog/voir_contacts.html',{'contacts':contacts})