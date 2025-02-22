import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.maximize_window()

def login():
    
    driver.get("https://www.saucedemo.com/")
    time.sleep(2) 


    busca_login = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    busca_login.click()
    time.sleep(1)

    busca_login.send_keys("visual_user")
    time.sleep(1)
    busca_login.send_keys(Keys.RETURN)

    
    busca_login = driver.find_element(By.XPATH, '//*[@id="password"]')
    busca_login.click()

    busca_login.send_keys("secret_sauce")
    time.sleep(1)
    busca_login.send_keys(Keys.RETURN)
    
    time.sleep(1)
    
    entrar = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    entrar.click()
    
    time.sleep(1)
    
    teste = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    teste.click()
    time.sleep(3)
    
    teste2 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    teste2.click()
    time.sleep(1)


    driver.quit()

login()
