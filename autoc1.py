import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.maximize_window()

def buscar_no_bing():
    
    driver.get("https://www.bing.com")
    time.sleep(3) 


    busca_box = driver.find_element(By.XPATH, '//*[@id="sb_form_q"]')
    busca_box.click()
    time.sleep(1)

    busca_box.send_keys("Python Selenium")
    time.sleep(1)
    busca_box.send_keys(Keys.RETURN)

    time.sleep(5)


    resultados = []


    itens = driver.find_elements(By.XPATH, '//li[@class="b_algo"]//h2/a')[:5]

    for item in itens:
        link = item.get_attribute("href")
        titulo = item.text 
        resultados.append((titulo, link))


    print("\nResultados encontrados:")
    for i, (titulo, link) in enumerate(resultados, 1):
        print(f"{i}. {titulo} - {link}")

    driver.quit()

buscar_no_bing()
