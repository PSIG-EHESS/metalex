import sys, os, re, diconorm
#Import des modules pour la ligne de commande, le travail sur un dossier et les expressions régulières
#Import également du dictionnaire qui contiendra les dictionnaires de mot avec leur identifiant pour chaque langue


for roots, dir, files in os.walk(sys.argv[1]):
	for filename in files:
		file_in = open(sys.argv[1] + filename, mode='r', encoding='utf-8')
		print("reading from "+sys.argv[1] + filename)
		file_out = open(sys.argv[2] + filename, mode='w')
		print("writing to "+ sys.argv[2] + filename)
		dico_termes = eval("diconorm." + sys.argv[3])
		#On appelle ici le dictionnaire et la variable à l'intérieur qui nous interessera en fonction de la langue
		for texte in file_in.readlines():
			for cle, valeur in dico_termes.items():
			#On va aller chercher les clés et les valeurs du dictionnaires pour ensuite itérer dessus
				if cle in texte:
					texte = texte.replace('>' + cle + '</txm:form>', '>' + cle + '</txm:form><txm:ana resp="#txm" type="#norm">'+valeur+'</txm:ana>')
					#Dans le cas où une des clés du dictionnaire est trouvée dans le texte, le script changera le 'none' en la valeur de la clé
			file_out.write(texte)
			
	file_in.close()
	file_out.close()

