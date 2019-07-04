import sys, os, re, dico_num
#Import des modules pour la ligne de commande, le travail sur un dossier et les expressions régulières
#Import également du dictionnaire qui contiendra les dictionnaires de mot avec leur identifiant pour chaque langue


for roots, dir, files in os.walk(sys.argv[1]):
	for filename in files:
		file_in = open(sys.argv[1] + filename, mode='r', encoding='utf-8')
		print("reading from "+sys.argv[1] + filename)
		file_out = open(sys.argv[2] + filename, mode='w')
		print("writing to "+ sys.argv[2] + filename)
		dico_termes = eval("dico_num." + sys.argv[3])
		#On appelle ici le dictionnaire et la variable à l'intérieur qui nous interessera en fonction de la langue
		for texte in file_in.readlines():
			texte = re.sub("</w>", '<txm:ana resp="#txm" type="#mlx">none</txm:ana></w>', texte)
			#On rajoute ici la balise qui servira d'identification de terme par la suite. Ici, elle a la même valeur pour chacun des mots, 'none'
			for cle, valeur in dico_termes.items():
			#On va aller chercher les clés et les valeurs du dictionnaires pour ensuite itérer dessus
				if cle in texte:
					texte = texte.replace('>' + cle +'</txm:ana><txm:ana resp="#txm" type="#mlx">none</txm:ana></w>', '>' + cle +'</txm:ana><txm:ana resp="#txm" type="#mlx">'+valeur+'</txm:ana></w>')
					#Dans le cas où une des clés du dictionnaire est trouvée dans le texte, le script changera le 'none' en la valeur de la clé
			texte = texte.replace("><", ">\n<")
			#Élement pas indispensable, permettant simplement une meilleure lecture du document XML par la suite.
			file_out.write(texte)
			
	file_in.close()
	file_out.close()

