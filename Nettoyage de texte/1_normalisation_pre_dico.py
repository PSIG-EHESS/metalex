import re, sys, os
#Import des modules à utiliser : 're' pour les expressions régulières et 'sys' pour la communication avec le terminal

def supprimer_ponctuation(texte):
    """ Supprimer les caractères de ponctuation d'un texte
    
    :param texte: Texte à nettoyer
    :type texte: str
    :returns: Texte sans ponctuation
    :rtype: str
    """
    ponctuation = '!:;",?'
	#Les points n'ont pas été inclus car les phrases doivent être conservées. 
	#Les tirets n'ont pas été inclus pour garder les mots écrits avec.
	#Les apostrophes ont également été conservées pour garder la cohérence du texte.
    for marqueur in ponctuation:
        texte = texte.replace(marqueur, "")
    return texte

def mise_a_la_ligne(texte):
	""" Structurer le texte pour garder les paragraphes d'origine 
	tout en supprimer tous les sauts de lignes originaux
	
	:param texte : Texte à nettoyer
	:type texte: str
	:returns: Texte avec une mise à la ligne par paragraphe
	:rtype: str
	"""

	#Transformation des points de fin de phrase avec saut de ligne en signe autre quelconque
	texte = re.sub('\.\n', '!\n', texte)
	#Suppression de tous les sauts de ligne et remplacement par un espace
	texte = re.sub('\n', ' ', texte)
	#Reconversion de tous les signes quelconque en point et ajout de saut de ligne après
	texte = re.sub('\! ', '.\n', texte)
	
	return texte
	
def normalisation_numerotation_chapitre(texte):
	"""Modification des numéros de chapitres pour 
	qu'ils soient chiffres arabes et non romains
	
	:param texte : Texte à nettoyer
	:type texte: str
	:returns: Début du texte avec des numéros de chapitres normalisés
	:rtype: str
	"""
	
	texte = re.sub('I\s?I\s?I.', '3', texte)
	texte = re.sub('I\s?I.', '2', texte)
	texte = re.sub('X\s?X\s?X\s?V\s?I.', '36', texte)
	texte = re.sub('X\s?X\s?X\s?I.', '31', texte)
	texte = re.sub('X\s?X\s?X.', '30', texte)
	texte = re.sub('X\s?I\s?V\.', '14', texte)
	texte = re.sub('X\s?I\s?I\s?I.', '13', texte)
	texte = re.sub('V\s?I\s?I.', '7', texte)
	texte = re.sub('§.\s?', '§', texte)	
	return texte



for root, dirs, files in os.walk(sys.argv[1]):
	for filename in files:
		file_in = open (sys.argv[1] + filename, mode='r', encoding='utf-8')
		#Fichier d'entrée que l'on va manipuler, 2ème argument dans le terminal, en mode lecture, encodage en UTF-8

		file_out = open (sys.argv[2].strip() + "/Norm" + filename, mode='w')
		#Fichier de sortie, 3ème argument dans le terminal, en mode écriture pour transformer le fichier d'entrée avec le script suivant
		#Ajout de la méthode strip() pour régler un problème qui se présentait lors de certaines transformations, où les créations de nouveaux fichiers ne fonctionnaient plus
		for line in file_in.readlines():
		#Application de la méthode .readlines() qui lit toutes les lignes du fichier dans une liste.
		#L'interpréteur pourra ainsi chercher des informations entre les lignes et ne pas être limité qu'à une seule.
			line = re.sub('[0-9]+\n', '', line)
			#Suppression des lignes avec les numéros de pages 
			line = line.replace('-\n', '')
			#Suppression des tirets suivis d'un saut de ligne
			line = line.replace('=\n', '')
			#LIGNE DE CODE À RAJOUTER POUR CORRESPONDRE AU MODÈLE ALLEMAND
			line = mise_a_la_ligne(line)
			#Application de la fonction mise_a_la_ligne pour structurer le texte
			line = normalisation_numerotation_chapitre(line)
			#Transformation du numéro de chapitre de chiffres romains à chiffres arabes
			line = line.replace('&', 'et')
			#Régularisation de la conjonction 'et' 
			line = line.lower()
			#Mise en minuscule de tout le texte
			line = supprimer_ponctuation(line)
			#Application de la fonction supprimer_ponctuation pour retirer les poncutations inutiles à l'analyse
			line = line.replace("'", ' ')
			line = line.replace("’", ' ')
			line = line.replace('.', ' ')
			#ELEMENTS A N'UTILISER QUE POUR AIDER A LA CORRECTION AVEC LE SPELLCHECKER
			file_out.write(line)	

		file_in.close()
		file_out.close()
		#Fermeture des deux fichiers après manipulation
