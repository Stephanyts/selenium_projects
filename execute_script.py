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

WebDriverWait(driver,7).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "card__image")))

element = driver.find_element(By.TAG_NAME, "footer")
driver.execute_script("arguments[0].scrollIntoView();", element)


assert "Around" in element.text

driver.quit()