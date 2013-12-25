#-*- coding: utf-8 -*-
from mini_url.forms import MiniURLForm
from mini_url.models import MiniURL
from django.shortcuts import render, redirect
import string
import random


def home(request):
    return render(request, 'mini_url/home.html', {'urls': MiniURL.objects.order_by('-nbAcces')})

def raccourcir(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = MiniURLForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            miniUrl = MiniURL()
            miniUrl.longURL = form.cleaned_data['longURL']
            miniUrl.pseudo = form.cleaned_data['pseudo']
            miniUrl.code = generer(10)
            miniUrl.save()
            return redirect('mini_url.views.home')

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = MiniURLForm()  # Nous créons un formulaire vide

    return render(request, 'mini_url/raccourcir.html', {'miniurl_form': form})


def redirection(request, code):
    miniUrl = MiniURL.objects.get(code=code)
    miniUrl.nbAcces += 1
    miniUrl.save()
    return redirect(miniUrl.longURL)


def generer(N):
    caracteres = string.letters + string.digits
    aleatoire = [random.choice(caracteres) for _ in xrange(N)]

    return ''.join(aleatoire)