import re, sys, os
#Import des modules à utiliser : 're' pour les expressions régulières et 'sys' pour la communication avec le terminal

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


for root, dirs, files in os.walk(sys.argv[1]):
	for filename in files:
		file_in = open (sys.argv[1] + filename, mode='r', encoding='utf-8')
		#Fichier d'entrée que l'on va manipuler, 2ème argument dans le terminal, en mode lecture, encodage en UTF-8

		file_out = open (sys.argv[2].strip() + "/Norm" + filename,"w")
		#Fichier de sortie, 3ème argument dans le terminal, en mode écriture pour transformer le fichier d'entrée avec le script suivant
		#Ajout de la méthode strip() pour régler un problème qui se présentait lors de certaines transformations, où les créations de fichiers ne fonctionnaient plus
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
			file_out.write(line)	

		file_in.close()
		file_out.close()
		#Fermeture des deux fichiers après manipulation
