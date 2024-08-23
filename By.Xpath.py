from datetime import time

from  selenium.webdriver.common.by import By

from selenium import webdriver

import time

# 2do ejercicio
driver = webdriver.Chrome() #inicia el controlador
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

time.sleep(5)

# Buscar el elemento
elements = driver.find_elements(By.XPATH, ".//img")
# condición el numero de elementos >1 pedido en el enunciado del ejercicio
assert len(elements) > 1

driver.quit()

#salida: no hay mas de 1 elemento