Python
======

Projets Python

Projet de test framework web DJango

Pour installation sous Windows 7 64bits : 

Interpréteur et Framework:

  1.Installer Python 2.7 : http://www.python.org/ftp/python/2.7.6/python-2.7.6.msi
  2.Ajouter le répertoire de scripts Python à la variable d'environnement Windows PATH : C:\Python27\Scripts 
  3.Installer setuptools : 
    1.télécharger ez_setup : https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
    2.exécuter ez-setup avec l'interpréteur python en ligne de commande : $ python ez_setup.py
  4.Intaller PIP : 
    1.télécharger get-pip.py : https://raw.github.com/pypa/pip/master/contrib/get-pip.py
    2.exécuter get-pip.py avec l'interpréteur python en ligne de commande : $ python get-pip.py
  5.Installer Django avec PIP : en ligne de commande, tapper : pip install django
  6.Installer pytz (Python TimeZone) : pip install pytz
  7.Installer PILLOW (gestion des uploads d'image)sous Windows7 64bits :  
    1.Installer le compilateur C++ pour Windows 64bits TDM-GCC : http://sourceforge.net/projects/tdm-gcc/files/TDM-GCC%20Installer/tdm64-gcc-4.8.1-3.exe/download
    2.Modifier le fichier suivant : C:\Python27\Lib\distutils\distutils.cfg (le créer s'il n'existe pas) 
    	1.Ajouter en quelque part dans le fichier les lignes
    	[build]
	compiler=mingw32
    3.Installer Python-DEV
    4.Lancer la commande pip install pillow
    
IDE: PyCharm 3.0, version commerciale pour gestion correcte de Django 
