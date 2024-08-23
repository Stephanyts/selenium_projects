from datetime import time

from selenium.webdriver.common.by import By

from selenium import webdriver

import time

driver = webdriver.Chrome() #inicia el controlador
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

time.sleep(5)

# Buscar el elemento
driver.find_element(By.CSS_SELECTOR, ".auth-form__title")

driver.quit()
