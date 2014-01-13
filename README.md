Projet de test framework web DJango
======

#### [Lien vers le tutoriel menant au code de ce projet](http://fr.openclassrooms.com/informatique/cours/developpez-votre-site-web-avec-le-framework-django)

Pour installation sous Windows 7 64bits : 

Interpréteur et Framework:

1. Installer Python 2.7 : http://www.python.org/ftp/python/2.7.6/python-2.7.6.msi
2. Ajouter le répertoire de scripts Python à la variable d'environnement Windows PATH : C:\Python27\Scripts 
3. Installer setuptools : 
    1. télécharger ez_setup : https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
    2. exécuter ez-setup avec l'interpréteur python en ligne de commande : $ python ez_setup.py
4. Intaller PIP : 
    1. télécharger get-pip.py : https://raw.github.com/pypa/pip/master/contrib/get-pip.py
    2. exécuter get-pip.py avec l'interpréteur python en ligne de commande : $ python get-pip.py
5. Installer Django avec PIP : en ligne de commande, tapper : pip install django
6. Installer pytz (Python TimeZone) : pip install pytz
7. Compiler et installer PILLOW (gestion des uploads d'image)sous Windows7 64bits :  
    1. Installer Visual C++ Express 2010 : http://go.microsoft.com/?linkid=9709952
    2. Définir la variable correspondante a VC++ 2010 (en ligne de commande) : SET VS90COMNTOOLS=%VS100COMNTOOLS%
    3. Lancer la commande pip install pillow
8. Installer Gettext (supérieur à 0.15)
    1. Télécharger **gettext-runtime-X.zip** et **gettext-tools-X.zip** depuis http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/
    2. Extraire le contenu des 2 fichiers zip vers C:\Program Files\gettext\bin
    3. Ajouter le chemin C:\Program Files (x86)\Gettext\bin à la variable d'entironnement Windows Path
    
    *Pour tester l'installation de gettext, il faut ouvrir une fenêtre de commande et tapper `xgettext --version`*
    
IDE: PyCharm 3.0, version commerciale pour gestion correcte de Django 
