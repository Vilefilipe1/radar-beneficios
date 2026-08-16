import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

def getGithub(driver, listaCompleta):
    driver.get('https://education.github.com/pack?sort=az')

    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for item in soup.find_all("div", class_="pack-offer-card"):
        nome = item.find("h3", class_="sr-only").text
        beneficio = (item.find_all("p")[1]).text
        
        listaCompleta.append({"Nome": nome, "Beneficio": beneficio, "Programa de Beneficios": "GitHub Student Developer Pack"})