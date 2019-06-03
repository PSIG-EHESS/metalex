from spellchecker import SpellChecker
import sys, os
#Import des modules pour lire les fichiers et pour les corriger

spell = SpellChecker(language=sys.argv[3].strip())
#spell = SpellChecker(language=None, local_dictionary='it.json.gz')
#Appel de la fonction de spellchecker en mentionnant la langue comme paramètre dans le terminal

for root, dirs, files in os.walk(sys.argv[1]):
	print(dirs)
	for filename in files:
		dico = {}
		#Création du dictionnaire pour contenir les mots à modifier et leur correction proposée
		file_in = open (sys.argv[1] + filename, mode='r', encoding='utf-8')
		print("reading from "+sys.argv[1] + filename)
		file_out = open (sys.argv[2].strip() + "/Ortho" + filename + ".py","w")
		print("writing to "+sys.argv[2] + "/Ortho" + filename + ".py")
		#Ouverture des fichiers d'entrée et de sortie
		for texte in file_in.readlines() :
		#Le fichier lit les textes en entier chacun à leur tour
			mots = texte.split()
			#Séparation du texte par mot, que l'on met dans une variable
			misspelled = spell.unknown(mots)
			#Recherche des mots inconnus par le module de SpellChecker
			for word in misspelled:
			#On  crée une boucle pour qu'il aille chercher dans cette liste de mots inconnus qui vient d'être crée
				dico[word] = spell.correction(word)
				#On met en place le dictionnaire avec en clé le mot inconnu et en valeur sa correction proposée
		file_out.write(filename+" = ")
		#Définition du nom du dictionnaire avec l'édition de Beccaria rattaché
		file_out.write(str(dico))
		#Ecriture du dictionnaire dans le fichier de sortie
		
	file_in.close()
	file_out.close()