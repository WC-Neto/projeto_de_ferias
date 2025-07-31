from pypdf import PdfReader
import re

leitor = PdfReader('.venv/arquivogeral.pdf')

for i, pagina in enumerate(leitor.pages):
    print(f'--- Processando página {i+1}')
    texto_da_pagina = pagina.extract_text()
    #print(texto_da_pagina)

info_album = dict()
lista_de_faixas = list()
compositores = list()
part_especial = list()

pattern = re.compile('[0-9]{2}.+/')

correspondencia = re.search(pattern, texto_da_pagina)
#print(correspondencia.group())

pattern = re.compile(r"^[0-9]{2}\.\s+(.*?)\s\s+(.*?)\s\s+(.*)", re.MULTILINE)
faixas_encontradas = pattern.findall(texto_da_pagina)
#print(faixas_encontradas)