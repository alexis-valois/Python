#-*- coding: utf-8 -*-
from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from models import MiniURL
from forms import MiniURLForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage  # Ne pas oublier l'importation



def liste(request, page=1):
    """Affichage des redirections"""
    minis_list = MiniURL.objects.order_by('-nb_acces')
    paginator = Paginator(minis_list, 5)  # 5 liens par page

    try:
           # La définition de nos URL autorise comme argument « page » uniquement des entiers,
           # nous n'avons pas à nous soucier de l'erreur PageNotAnInteger
           minis = paginator.page(page)
    except EmptyPage:
           # Nous vérifions toutefois que nous ne dépassons pas la limite de page
           # Par convention, nous renvoyons la dernière page dans ce cas
           minis = paginator.page(paginator.num_pages)

    return render(request, 'mini_url/liste.html', locals())


class URLCreate(CreateView):
    model = MiniURL
    template_name = 'mini_url/nouveau.html'
    form_class = MiniURLForm
    success_url = reverse_lazy(liste)


class URLUpdate(UpdateView):
    model = MiniURL
    template_name = 'mini_url/nouveau.html'
    form_class = MiniURLForm
    success_url = reverse_lazy(liste)

    def get_object(self, queryset=None):
           code = self.kwargs.get('code', None)
           return get_object_or_404(MiniURL, code=code)


    def form_valid(self, form):
           self.object = form.save()
           messages.success(self.request, "Votre profil a été mis à jour avec succès.")  # Envoi d'un message à l'utilisateur
           return HttpResponseRedirect(self.get_success_url())


class URLDelete(DeleteView):
    model = MiniURL
    context_object_name = "mini_url"
    template_name = 'mini_url/supprimer.html'
    success_url = reverse_lazy(liste)

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(MiniURL, code=code)

def nouveau(request):
    """Ajout d'une redirection"""
    if request.method == "POST":
        form = MiniURLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(liste)
    else:
        form = MiniURLForm()

    return render(request, 'mini_url/nouveau.html', {'form':form})


def redirection(request, code):
    """Redirection vers l'URL enregistrée"""
    mini = get_object_or_404(MiniURL, code=code)
    mini.nb_acces += 1
    mini.save()

    return redirect(mini.url, permanent=True)