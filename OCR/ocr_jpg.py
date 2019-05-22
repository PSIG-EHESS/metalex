# input1 : dossier, input2 : language model (deu_frak, deu, fra, eng, ita, ...)

import sys, os
from PIL import Image
import pytesseract

# ex:  python3 handleocr.py all/Beccaria_DE_1766_HAB_Kap36/out deu_frak
if len(sys.argv) != 3:
	#print("python3 handleocr.py <dossier> deu_frak|deu")
	print("La requête n'est pas correcte. Veuillez vérifier les arguments.")
	sys.exit()
	
for i in os.listdir(sys.argv[1]):
	if i.endswith("jpg"):
		print("reading: "+sys.argv[1]+"/"+i)
		im = Image.open(sys.argv[1]+"/"+i)
		text = pytesseract.image_to_string(im, lang = sys.argv[2])
		file = open(sys.argv[1]+"/"+i+".txt","w") 
		file.write(text) 
		print("writing OCR result to: "+sys.argv[1]+"/"+i+".txt")
