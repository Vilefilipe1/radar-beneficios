from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from src.scrapers.hapvida import *
from src.scrapers.surpreenda import *
from src.scrapers.github import *
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

firefox_options = FirefoxOptions()
firefox_options.add_argument("--headless")
driver = webdriver.Firefox(options=firefox_options)

REGIAO = os.getenv("REGIAO")

def main():
    regiao = "Sergipe"  # Região desejada
    listaCompleta = []

    getHapvida(driver, listaCompleta, regiao)
    getSurpreenda(driver, listaCompleta)
    getGithub(driver, listaCompleta)

    driver.close()

    # print(listaCompleta)
    # print(len(listaCompleta))

    df = pd.DataFrame(listaCompleta)
    df = df.sort_values("Nome")
    df.reset_index(drop=True, inplace=True)

    df.to_csv("Ofertas.csv")
    df.to_json("Ofertas.json", orient="records", force_ascii=False, indent=2)   

if __name__ == "__main__":
    main()
