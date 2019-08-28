#!/bin/bash
#Utilisation du script avec les expressions régulières
python3 script_regex_normalisation.py ../../../TXM-0.8.0/corpora/FR303136/txm/FR303136/ ../../Travail\ TXM/Corpus/Norm/Fr/CHAP30 remplacement_fr
python3 script_regex_normalisation.py ../../../TXM-0.8.0/corpora/EN303136/txm/EN303136/ ../../Travail\ TXM/Corpus/Norm/En/CHAP30 remplacement_en
python3 script_regex_normalisation.py ../../../TXM-0.8.0/corpora/IT303136/txm/IT303136/ ../../Travail\ TXM/Corpus/Norm/It/CHAP30 remplacement_it
#Utilisation du script avec le module XML pour Python
python3 script_xml_normalisation.py ../../../TXM-0.8.0/corpora/FR303136/txm/FR303136/ ../../Travail\ TXM/Corpus/Norm/Fr/CHAP30/ remplacement_fr
python3 script_xml_normalisation.py ../../../TXM-0.8.0/corpora/EN303136/txm/EN303136/ ../../Travail\ TXM/Corpus/Norm/En/CHAP30/ remplacement_en
python3 script_xml_normalisation.py ../../../TXM-0.8.0/corpora/IT303136/txm/IT303136/ ../../Travail\ TXM/Corpus/Norm/It/CHAP30/ remplacement_it
#Appel du script, du dossier d'entrée (qui part ici de la production XML-TEI TXM du logiciel TXM) puis du dossier de sortie
#Enfin, on appelle comme pour les autres scripts avec un dictionnaire, la variable avec le contenu recherché pour chaque langue
#Mettre en commentaire l'un des deux groupes en fonction du script utilisé
