from selenium import webdriver

import time

driver = webdriver.Chrome() #inicia el controlador
driver.maximize_window() #para abrir en pantalla completa

driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=es')

# 1er ejercicio
current_url = driver.current_url #para guardar la URL en current_url
#comprobar que '/signin' se agrego en current_url
assert '/signin' in driver.current_url

driver.quit() #cerrar el navegador