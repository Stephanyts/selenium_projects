from selenium.webdriver.common.by import By

from selenium import webdriver

from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait

import time

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

time.sleep(1)

# Buscar el elemento
driver.find_element(By.ID, "email").send_keys("stephanyts54@gmail.com")
driver.find_element(By.ID, "password").send_keys("wtfisthisshit")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "profile__image")))

driver.find_element(By.CLASS_NAME, "profile__image").click()

# Insertar enlace a la foto de perfil en el campo enlace usando la variable avatar_url
avatar_url = "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png"
driver.find_element(By.ID, "owner-avatar").send_keys(avatar_url)
# Hacer click en guardar
driver.find_element(By.CLASS_NAME, "button popup__button").click()
# Guardar el valor del atributo de estilo para el elemento de foto de perfil en la variable style
style = driver.find_element(By.CLASS_NAME, "profile__image")

WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "profile__image")))

assert style.get_attribute('style') == "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png"

driver.quit()