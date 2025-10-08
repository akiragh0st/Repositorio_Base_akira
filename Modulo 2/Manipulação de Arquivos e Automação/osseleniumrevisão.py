
# os.listdir()
# os.rename()
# os.remove()
# import os

# os.mkdir("ads")
# os.rename("ads", "p")
# print("Pastas:", os.listdir())

# webdriver.Chrome()abre o chrome
# find_element() acha o elemento do codigo
# send_keys() vai mandar texto e teclas
# click() clica 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Brave()
navegador.get("https://www.google.com")
caixa = navegador.find_element(By.NAME, "q")
caixa.send_keys("Python", Keys.ENTER)