import time
from bs4 import BeautifulSoup

def getSurpreenda(driver, listaCompleta):
    driver.get('https://surpreenda.naotempreco.com.br/ofertas/')

    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    elementoGrupo = soup.find("ul", class_="c-btdZiW")
    for item in elementoGrupo.find_all("li", class_="c-PJLV"):
        nome = item.find("h3").text
        beneficio = item.find("p").text
        listaCompleta.append({"Nome": nome, "Beneficio": beneficio, "Programa de Beneficios": "Surpreenda"})