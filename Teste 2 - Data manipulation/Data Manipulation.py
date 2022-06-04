import camelot
import pandas as pd
 
print("Importando PDF, isso pode demorar um pouco...")
tables=camelot.read_pdf("Anexo_I.pdf", pages = '3-200', flavor = 'stream')
print("PDF importado, fazendo alterações...")

for table in tables:
    table.df.replace(['OD'],'Seg. Odontológica', inplace=True)
    table.df.replace(['AMB'],'Seg. Ambulatorial', inplace=True)

print("Comprimindo os arquivos modificados...")
tables.export("Teste_{Leandro_Bucci}", compress = True)

