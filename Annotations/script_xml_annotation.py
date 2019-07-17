import xml.etree.ElementTree as ET
# Import du module nécessaire à la lecture d'un texte dans un fichier XML
import sys, dico_alpha, os
# Import des autres modules nécessaires à la bonne exécution du script

for roots, dir, files in os.walk(sys.argv[1]):
	for filename in files:
		tree = ET.parse(sys.argv[1] + filename)
		# Lecture de l'arbre du fichier XML, qui est placé dans une variable
		print("reading from "+sys.argv[1] + filename)
		dico_termes = eval("dico_alpha." + sys.argv[3])
		#Appel du dictionnaire
		namespaces = {'txm': 'http://textometrie.org/1.0', 'tei' : 'http://www.tei-c.org/ns/1.0'}
		ET.register_namespace('txm', 'http://textometrie.org/1.0')
		ET.register_namespace('tei', 'http://www.tei-c.org/ns/1.0')
		# Ajout des namespaces contenus dans les balises du fichier XML et enregistrement pour qu'ils ressortent correctement dans le fichier XML
		for mot in tree.iterfind('.//tei:w', namespaces):
		#Recherche des éléments enfants de la balise (on mentionne qu'un namespace est à prendre en compte)
			mlx = ET.SubElement(mot, 'txm:ana')
			# Ajout d'un nouvel enfant à la balise <w>
			mlx.set("resp", '#txm')
			mlx.set("type", "#mlx")
			# Ajout de ses attributs
			mlx.text = "none"
			# Ajout de sa valeur
			for cle, valeur in dico_termes.items():
			# Appel des cles et valeurs du dictionnaire
				if cle in mot.itertext():
				# Recherche toutes les valeurs textes dans les sous-éléments et ne retient que ceux qui correspondent à une des clés du dictionnaire
					mlx.text = valeur
					# Si la condition est remplie, le texte de la balise "mlx" est remplacé par la valeur de la clé
		tree.write(sys.argv[2] + filename, encoding='UTF-8')
		print("writing to "+ sys.argv[2] + filename)
		# Tout cela est écrit dans un nouveau fichier