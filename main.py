from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

driver = webdriver.Firefox()
listaCompleta = []

def getHapvida():
    driver.get('https://clube.hapvida.com.br/')

    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    while (soup.find("button", string="Carregar mais parceiros") != None):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

    for item in soup.find_all("div", class_="item"):
        nome = item.find("h4").span.text
        beneficio = item.find("div", class_="discount").span.text

        listaCompleta.append({"Nome": nome, "Beneficio": beneficio, "Programa de Beneficios": "Hapvida"})

def getSurpreenda():
    driver.get('https://surpreenda.naotempreco.com.br/ofertas/')

    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    elementoGrupo = soup.find("ul", class_="c-btdZiW")
    for item in elementoGrupo.find_all("li", class_="c-PJLV"):
        nome = item.find("h3").text
        beneficio = item.find("p").text
        listaCompleta.append({"Nome": nome, "Beneficio": beneficio, "Programa de Beneficios": "Surpreenda"})

# getHapvida()
getSurpreenda()
# print(listaCompleta)
print(len(listaCompleta))

driver.close()

df = pd.DataFrame(listaCompleta)
df = df.sort_values("Nome")
df.reset_index(drop=True, inplace=True)
df.to_csv("Hapvida+Surpreenda.csv")
