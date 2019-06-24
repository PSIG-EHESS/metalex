# metalex
Métalexicographie numérique des langues historiques du droit en Europe. Projet pilote à partir de l’exemple de Dei delitti e delle pene de Cesare Beccaria.

Pour travailler sur le projet, il est nécessaire tout d'abord de travailler avec les textes à disposition pour qu'il soit exploitable.
On fournira ainsi ici les scripts nécessaires à aider cette exploitation et plus tard réalisés une analyse.
Le dossier "OCR" comprend deux scripts pour permettre la transcription des textes.
Le dossier "Nettoyage_texte" comprend quatre scripts pour permettre de mettre en forme et de corriger autant que permis les textes.
Le dossier "Annotations" permet de rajouter des balises dans une version XML-TEI TXM de ces transcriptions pour une analyse ultérieur sur TXM.

Les scripts sont écrits dans le langage Python et utilise un module qui permet d'appeler les arguments nécessaires à chaque script dans l'interpréteur de commance pour obtenir les résultats que l'on veut.
Pour exécuter ces scripts, il faudra taper :

python3 nom_du_script.py arg1, arg2, 

Le nombre d'arguments dépendra du contenu du script. Dans le cas du script '4_correction.py' du dossier 'Nettoyage_texte', le dernier argument sera une variable, présent dans le fichier python importé dans le script et qui correspondra au nom du dictionnaire à aller chercher.
