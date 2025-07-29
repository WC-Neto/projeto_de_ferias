from pypdf import PdfReader

leitor = PdfReader('arquivogeral.pdf')

for i, pagina in enumerate(leitor.pages):
    print(f'--- Processando página {i+1}')
    texto_da_pagina = pagina.extract_text()
    print(texto_da_pagina)

info_album = dict()
lista_de_faixas = list()
compositores = list()
part_especial = list()