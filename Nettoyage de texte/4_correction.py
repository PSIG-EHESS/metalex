import sys, dico
#Import du module pour les arguments et du fichier python qui contiendra les dictionnaires requis

file_in = open (sys.argv[1], mode='r', encoding='utf-8')
file_out = open (sys.argv[2],"w", encoding='utf-8')
#Appel des fichiers d'entrée et de sortie


dico_var = eval("dico."+sys.argv[3])
#Définition d'une variable qui contiendra le dictionnaire importé avec le script + un argument donné dans le terminal qui ira chercher le bon dictionnaire pour chacune des demande
#La méthode eval() permet d'appeler le dictionnaire sans que le script python ne considère cela comme une erreur. 

for texte in file_in:
#On extraie un texte du fichier d'entrée
	for cle, valeur in dico_var.items():
	#On définit des variables qui contiendront les clés et valeurs du dictionnaires
		if cle in texte:
		#On recherche ces clés dans le texte que le fichier lit
			texte = texte.replace(cle, valeur)
			#On remplace les mots qui correspondent aux clés du dictionnaires, par la valeur de ces dictionnaire

	file_out.write(texte)
	#On inscrit cela dans le texte. L'indentation est importante car sinon Python ne saura pas correctement inscrire ce qui est nécessaire.


file_in.close()
file_out.close()