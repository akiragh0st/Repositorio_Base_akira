import requests
from bs4 import BeautifulSoup

resposta = requests.get("https://github.com/akiragh0st")
site = BeautifulSoup(resposta.text, "html.parser")
titulo = site.find("h1").text

print("Coisas do github", titulo)
# requests.get(URL): Faz uma requisição HTTP.
# BeautifulSoup(html, "html.parser"): Interpreta o HTML.
# HTML = estrutura do site.
# CSS = estilo visual.
