#-*- coding: utf-8 -*-
__author__ = 'Alexis'
from django import forms
from models import MiniURL


class MiniURLForm(forms.ModelForm):
    class Meta:
        model = MiniURL
        fields = ('longURL','pseudo')