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

for link in links:
    post_text=link.get('href') # de cada <a> sacar la href
    if post_text!=None: # las None no son iterables
        if '/posts/' in post_text: #seleccionar los posts
            post_text=post_text[7:-1] #limpiar la cadena '/posts/'
            no_dash_text='"'+post_text.replace('-',' ')+'"' #añadir ""
            result=inflection.titleize(no_dash_text) #primera en mayus
            print(result)
