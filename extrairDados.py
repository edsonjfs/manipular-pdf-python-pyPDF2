from PyPDF2 import PdfFileReader
import re
 

FILE_PATH = 'resultado.pdf'

x = PdfFileReader(open(FILE_PATH, 'rb'))
print(x)
print(x.getNumPages())

