import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

def getHapvida(driver, listaCompleta, regiao):
    driver.get('https://clube.hapvida.com.br/')

    time.sleep(2)

    # Aceitar cookies se o banner aparecer                                                                                                                                                                                                                 
    try:                                                                                                                                                                                                                                                   
        botao_cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")                                                                                                                                                                          
        botao_cookies.click()                                                                                                                                                                                                                              
        time.sleep(1)                                                                                                                                                                                                                                      
    except Exception:                                                                                                                                                                                                                                      
        pass  

    # Seleciona a região "Sergipe" no modal de localidades
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    botao_localidade = driver.find_element(By.CLASS_NAME, "locations-button-trigger")  
    botao_localidade.click()
    time.sleep(1)

    xpath_expr = f"//small[contains(normalize-space(.), '{regiao}') or contains(normalize-space(.), '{regiao}')]"   
    driver.find_element(By.XPATH, xpath_expr).click()
    time.sleep(5)

    # XPath flexível para 'Ver Mais' ou 'Ver mais' ignorando espaços extras e tags filhas                                                                                                                                                                  
    xpath_expr = "//button[contains(normalize-space(.), 'Ver Mais') or contains(normalize-space(.), 'Ver mais')]"      
    while True:
        # Busca apenas elementos que estão de fato visíveis na tela                                                                                                                                                                                        
        botoes = [btn for btn in driver.find_elements(By.XPATH, xpath_expr) if btn.is_displayed()]                                                                                                                                                         
                                                                                                                                                                                                                                                            
        if not botoes:                                                                                                                                                                                       
            break 

        btn = botoes[0]                                                                                                                                                                                                                                    
        try:                                                                                                                                                                                                                                               
            # Rola até o botão e clica via JavaScript                                                                                                                                                                                                      
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)                                                                                                                                                                  
            # time.sleep(1)                                                                                                                                                                                                                                  
            driver.execute_script("arguments[0].click();", btn)                                                                                                                                                                                            
            time.sleep(1)  # Aguarda o carregamento dos novos itens                                                                                                                                                                                        
        except Exception as e:                                                                                                                                                                                                                             
            print(f"[HAPVIDA] Fim ou erro ao tentar clicar no botão: {e}")                                                                                                                                                                                           
            break         

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for item in soup.find_all("a", class_="sc-gUrTyy"):
        nome = item.find("div", class_="sc-iMfspA").span.text
        beneficio = item.find("div", class_="sc-jfSnVq").span.text
        listaCompleta.append({"Nome": nome, "Beneficio": beneficio, "Programa de Beneficios": "Hapvida"})