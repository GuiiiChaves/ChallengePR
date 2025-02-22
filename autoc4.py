from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)
driver.maximize_window()

def open_first_website():
    driver.get("https://demo.automationtesting.in/FileDownload.html")

    txt_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="textbox"]'))
    )

    driver.execute_script("arguments[0].scrollIntoView();", txt_box)
    time.sleep(1)

    txt_box.click()
    txt_box.send_keys("Boa tarde, Guilherme! Informamos que você foi aprovado para a nossa vaga de estágio na PR Promotora.")
    
    download_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="createTxt"]'))
    )
    
    download_button.click()
    
    download_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="link-to-download"]'))
    )
    download_link.click()
    
    time.sleep(2)
    
    pdf_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pdfbox"]'))
    )
    
    driver.execute_script("arguments[0].scrollIntoView();", pdf_box)
    time.sleep(1)
    
    pdf_box.click()
    pdf_box.send_keys("Boa tarde, Guilherme! Informamos que você foi aprovado para a nossa vaga de estágio na PR Promotora.")
    
    download_button2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="createPdf"]'))
    )
    
    download_button2.click()
    
    download2_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="pdf-link-to-download"]'))
    )
    download2_link.click()

open_first_website()

time.sleep(10)
driver.quit()
