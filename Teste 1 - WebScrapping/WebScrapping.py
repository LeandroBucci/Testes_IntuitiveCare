import requests
import os
import zipfile
from bs4 import BeautifulSoup

def main():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
    url = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    with zipfile.ZipFile('Files-Zipped.zip', 'w') as zipf:
        for i in soup.select('div#parent-fieldname-text > h3 ~ p'):
            link = i.a.get('href')
            if 'Anexo' in link:
                basename = os.path.basename(link)
                response = requests.get(link)
                file = open(basename, 'wb')
                file.write(response.content)
                zipf.write(basename, compress_type = zipfile.ZIP_DEFLATED)
                file.close()
                print("File Downloaded:",basename)
    print("Files Zipped")

if __name__ == '__main__':
    main()

