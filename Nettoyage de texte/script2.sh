#!/bin/bash
python3 2_verification_orthographique.py ../../Normalisation/All/Chap30-31-36/ ../../Orthographe/De/Chap30-31-36/ de
python3 2_verification_orthographique.py ../../Normalisation/En/Chap30-31-36/ ../../Orthographe/En/Chap30-31-36/ en
python3 2_verification_orthographique.py ../../Normalisation/Fr/Chap30-31-36/ ../../Orthographe/Fr/Chap30-31-36/ fr
#python3 2_verification_orthographique.py ../../Normalisation/It/Chap30-31-36/ ../../Orthographe/It/Chap30-31-36/
#Création des dictionnaires d'orthographe qui permettra de relever les erreurs orthographiques du texte
#La démarche est la même que pour le premier script mais il est nécessaire de rajouter à la fin la langue du dictionnaire
#Le cas de l'italien est particulier, puisque le dictionnaire n'existe pas directement dans le module pyspellchecker
#Il est nécessaire de l'appeler dans le script même, donc il ne figure pas dans la requête du terminal
