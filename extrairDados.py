from PyPDF2 import PdfFileReader
import code
import re
 
FILE_PATH = 'resultado.pdf'

pdf_original = PdfFileReader(open(FILE_PATH, 'rb'))

pagina_0 = pdf_original.getPage(0)
pagina_1 = pdf_original.getPage(1)
pagina_2 = pdf_original.getPage(2)

pagina_0.mergePage(pagina_1)
pagina_0.mergePage(pagina_2)

pagina = pagina_0.extractText()

pagina = pagina[1449:11952]

pagina = pagina.replace("\n", "")
pagina = pagina.replace(" ", "")
pagina = pagina.replace("6.88.", "6.88")
pagina = pagina.replace("3119.0", "119.0")

pagina = pagina.split("/")



for x in range(0,118):
    pagina[x] = pagina[x].split(",")
    for y in range(2,len(pagina[x])):
        pagina[x][y] = float (pagina[x][y])
        
for x in range(0,118):
    pagina[x][9] = pagina[x][6] + pagina[x][9]

def maior(e):
    return e[9]

pagina.sort(reverse = True, key=maior)

for x in range(0, 118):
    print(pagina[x])





