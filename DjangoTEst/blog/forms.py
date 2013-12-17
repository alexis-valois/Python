#-*- coding: utf-8 -*-
__author__ = 'Alexis'
from django import forms
from models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article


class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label=u"Votre adresse mail")
    renvoi = forms.BooleanField(help_text=u"Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)


    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')

        if sujet and message:  # Est-ce que sujet et message sont valides ?
            if "pizza" in sujet and "pizza" in message:
                msg = u"Vous parlez déjà de pizzas dans le sujet, n'en parlez plus dans le message !"
                self._errors["message"] = self.error_class([msg])

                del cleaned_data["message"]

        return cleaned_data