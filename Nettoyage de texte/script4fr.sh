#!/bin/bash
python3 4_correction_orthographique.py ../../Normalisation/Fr/Chap30-31-36/NormBeccaria-fr-1766-transcr.txt ../../Finalisation/Fr/Chap30-31-36/Beccaria_fr1_1_1766.txt beccaria_fr1_1_1766
python3 4_correction_orthographique.py ../../Normalisation/Fr/Chap30-31-36/NormBeccaria-fr-1773-transcr.txt ../../Finalisation/Fr/Chap30-31-36/Beccaria_fr2_1_1773.txt beccaria_fr2_1_1773
python3 4_correction_orthographique.py ../../Normalisation/Fr/Chap30-31-36/NormBeccaria-fr-1782-transcr.txt ../../Finalisation/Fr/Chap30-31-36/Beccaria_fr2_2_1782.txt beccaria_fr2_2_1782
python3 4_correction_orthographique.py ../../Normalisation/Fr/Chap30-31-36/NormBeccaria-fr-1784-transcr.txt ../../Finalisation/Fr/Chap30-31-36/Beccaria_fr2_3_1784.txt beccaria_fr2_3_1784
python3 4_correction_orthographique.py ../../Normalisation/Fr/Chap30-31-36/NormBeccaria-fr-1794-transcr.txt ../../Finalisation/Fr/Chap30-31-36/Beccaria_fr2_4_1794.txt beccaria_fr2_4_1794
python3 4_correction_orthographique.py ../../Normalisation/Fr/Chap30-31-36/NormBeccaria-fr-1797-Chaillou-transcr.txt ../../Finalisation/Fr/Chap30-31-36/Beccaria_fr2_5_1797Ch.txt beccaria_fr2_5_1797Ch
python3 4_correction_orthographique.py ../../Normalisation/Fr/Chap30-31-36/NormBeccaria-fr-1797-Morellet-transcr.txt ../../Finalisation/Fr/Chap30-31-36/Beccaria_fr1_2_1797Mo.txt beccaria_fr1_2_1797Mo
#Exemple d'une utilisation du 4ème script avec le chap30/31/36 en français
#Contrairement aux fois précédentes, ce n'est plus un dossier que l'on appelle mais un fichier qui sera lié à une variable du dictionnaire importé dans le script
#Le nom de la variable dans le dictionnaire correspond au nom du nouveau fichier texte, qui sera le produit final de tout le nettoyage du texte
