from selenium.webdriver.common.by import By

from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signup")
time.sleep(2)

class loginPageAround:
    #Localizador de campo correo electronico
    email_field = (By.ID, 'email')
    # Localizador de campo contrasena
    password_field = (By.ID, "password")
    # Localizador de boton registrarse
    registration_button = (By.CLASS_NAME, 'auth-form__button')

    # Constructor de clase
    def __init__(self, driver):
        self.driver = driver

    # Metodo comprueba si se puede hacer clic en el boton registrarse
    def check_sign_in_is_enabled(self):
        return self.driver.find_element(*self.registration_button).is_enabled()

    #Metodo hace clic en el boton registarse
    def click_registration_button(self):
        self.driver.find_element(*self.registration_button).click()

    # Metodo para validar texto del botón registrarse
    def check_text_registration_button(self):
        Registration_button_text = driver.find_element(self.registration_button).text
        assert Registration_button_text == 'Registrarse'