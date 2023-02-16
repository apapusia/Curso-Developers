import requests
import inflection
from bs4 import BeautifulSoup

#conseguir el html de la web
response=requests.get('https://dailysmarty.com/topics/python')
html_doc=response.content
#hacer legibles el codigo
soup = BeautifulSoup(html_doc, 'html.parser')

#seleccionar las <a>
links=soup.find_all('a')

def titles_generator(links):
    titles=[]

    def post_formatter(url):
        if url!=None: # los None no son iterables
            if 'posts' in url: #si existe la palabra posts en la url
                url=url.split('/')[-1] #trocear la url y quedarme con la ultima cadena
                url=url.replace('-',' ')
                url=inflection.titleize(url)
                titles.append(url)
                

    for link in links:
        post_formatter(link.get('href'))
    return titles

titles=titles_generator(links)  #para imprimir cada titulo en dif lineas
for title in titles:
    print(title)
    
