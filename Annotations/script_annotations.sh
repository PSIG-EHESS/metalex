#!/bin/bash
python3 annotations.py ../../Travail\ TXM/Corpus/Norm/Fr/CHAP30/ ../../Travail\ TXM/Corpus/Num/ termes_fr
python3 annotations.py ../../Travail\ TXM/Corpus/Norm/En/CHAP30/ ../../Travail\ TXM/Corpus/Num/ termes_en
python3 annotations.py ../../Travail\ TXM/Corpus/Norm/It/CHAP30/ ../../Travail\ TXM/Corpus/Num/ termes_it
#On appelle ici le script, le dossier d'entrée, de sortie et enfin une variable contenue dans le dictionnaire importé dans le script
