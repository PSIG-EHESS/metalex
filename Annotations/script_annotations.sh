#!/bin/bash
#Utilisation du script contenant les expressions régulières
python3 script_regex_annotation.py ../../Travail\ TXM/Corpus/Norm/Fr/CHAP30/ ../../Travail\ TXM/Corpus/Num/ termes_fr
python3 script_regex_annotation.py ../../Travail\ TXM/Corpus/Norm/En/CHAP30/ ../../Travail\ TXM/Corpus/Num/ termes_en
python3 script_regex_annotation.py ../../Travail\ TXM/Corpus/Norm/It/CHAP30/ ../../Travail\ TXM/Corpus/Num/ termes_it
#Utilisation du script contenant le module XML pour Python
python3 script_xml_annotation.py ../../Travail\ TXM/Corpus/Norm/Fr/CHAP30/ ../../Travail\ TXM/Corpus/Num/ termes_fr
python3 script_xml_annotation.py ../../Travail\ TXM/Corpus/Norm/En/CHAP30/ ../../Travail\ TXM/Corpus/Num/ termes_en
python3 script_xml_annotation.py ../../Travail\ TXM/Corpus/Norm/It/CHAP30/ ../../Travail\ TXM/Corpus/Num/ termes_it
#On appelle ici le script, le dossier d'entrée, de sortie et enfin une variable contenue dans le dictionnaire importé dans le script
#Mettre en commentaire l'un des deux groupes en fonction du script utilisé
