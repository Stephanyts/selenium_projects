from selenium import webdriver

from  selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

time.sleep(5)

#Buscar elementos
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "password")

# Probar el atributo placeholder para cada elemento
assert email.get_attribute('placeholder') == "Correo electrónico"
assert password.get_attribute('placeholder') == "Contraseña"

print(email.get_attribute('placeholder'))
print(password.get_attribute('placeholder'))

driver.quit()