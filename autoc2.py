from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()

def acessar_mercado_livre():
    driver.get("https://www.mercadolivre.com.br")


    busca_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="cb1-edit"]'))
    )
    busca_box.send_keys("iPhone")
    busca_box.send_keys(Keys.RETURN)


    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//ol/li"))
    )


    produtos = []

    
    itens = driver.find_elements(By.XPATH, "//ol/li//h3/a")[:3]

    for item in itens:
            link = item.get_attribute("href")
            if link:
                nome_produto = link.split("/")[3].replace("-", " ").title()
                produtos.append((nome_produto, link))



    print("\nProdutos encontrados:")
    for i, (nome_produto, link) in enumerate(produtos, 1):
        print(f"{i}. {nome_produto} - {link}")


    driver.quit()

acessar_mercado_livre()
