# input1 : dossier, input2 : language model (frk, deu, fra, eng, ita, ...)

import sys, os
from PIL import Image
import pytesseract

# ex:  python3 ocr_tiff.py OCR/Deu/all2-1(1767)/Introduction/ frk
if len(sys.argv) != 3:
	print("La requête n'est pas correcte. Veuillez vérifier les arguments.")
	sys.exit()
	
for i in os.listdir(sys.argv[1]):
	if i.endswith("tif"):
		print("reading: "+sys.argv[1]+"/"+i)
		im = Image.open(sys.argv[1]+"/"+i)
		text = pytesseract.image_to_string(im, lang = sys.argv[2])
		file = open(sys.argv[1]+"/"+i+".txt","w") 
		file.write(text) 
		print("writing OCR result to: "+sys.argv[1]+"/"+i+".txt")
