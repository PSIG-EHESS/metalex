# Metalex
Métalexicographie numérique des langues historiques du droit en Europe. Projet pilote à partir de l’exemple de Dei delitti e delle pene de Cesare Beccaria.

Pour travailler sur le projet, il est nécessaire tout d'abord de travailler avec les textes à disposition pour qu'ils soient exploitables.
On fournira ainsi ici les scripts nécessaires à aider cette exploitation et plus tard réaliser une analyse :

* Le dossier "OCR" comprend deux scripts pour permettre la transcription des textes.
* Le dossier "Nettoyage_texte" comprend quatre scripts pour permettre de mettre en forme et de corriger, autant que permis, les textes.
* Le dossier "Annotations" comprend un script qui permet de rajouter des balises dans une version XML-TEI TXM de ces transcriptions pour une analyse ultérieure sur TXM.

Les scripts sont écrits dans le langage Python (avec la version Python 3.6.7 ici) et utilise un module qui permet d'appeler les arguments nécessaires à chaque script dans l'interpréteur de commande (sys) pour obtenir les résultats que l'on veut.
Pour exécuter ces scripts, il faudra inscrire dans le terminal, depuis le dossier où se trouve le script : 

```bash
python3 nom_du_script.py dossier_d'entrée dossier_de_sortie
```

Le nombre d'arguments dépendra après du contenu du script. Dans deux des dossiers ("Nettoyage_texte" et "Annotations") ont été rajoutés les scripts shell utilisés pour permettre d'exécuter les scripts correctement et selon nos besoins. Chacun de ces scripts shell se basent sur un travail avec un chapitre choisi (Chap30/31/36) pour illustrer les manipulations réalisées.


Pour exécuter certains des scripts, il faut au préalable installer sur son environnement de travail quelques modules indispensables : 
* Pour faire fonctionner les scripts d'OCR, il est essentiel d'installer Tesseract. Il suffit pour cela de suivre les instructions présentes sur le Github du module : [Tesseract](https://github.com/tesseract-ocr/tesseract "Repository Tesseract")
