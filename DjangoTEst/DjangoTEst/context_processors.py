#-*- coding:utf-8 -*-
__author__ = 'Alexis'
from datetime import datetime


def get_infos(request):
    date_actuelle = datetime.now()
    return {'date_actuelle': date_actuelle}

