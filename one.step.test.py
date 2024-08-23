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
    sign_in_button = (By.CLASS_NAME, 'auth-form__button')
    # localizador de botón agregar publicación
    click_add_new_place_button = (By.CLASS_NAME, 'profile__add-button')
    # Localizador para introducir nombre del lugar nuevo
    set_name = (By.ID, 'place-name')
    # Localizador para agregar nuevo enlace a foto
    set_link_to_picture_field = (By.ID, 'place-link')
    # Localizador boton guardar
    click_save_button = (By.XPATH, "//button[@class='button popup_button']")

    # Constructor de clase
    def __init__(self, driver):
        self.driver = driver

    # Método rellena campo correo electronico
    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys('stephanyts54@gmail.com')

    #Método rellena campo contrasena
    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys('wtfisthisshit')

     # Metodo hace clic en el boton registarse
    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    def click_add_place_button(self):
        self.driver.find_element(*self.click_add_new_place_button).click()

    def setname(self, name):
        self.driver.find_element(*self.set_name).send_keys('Tokio, Japon')

    def set_link_to_picture(self, picture):
        self.driver.find_element(*self.set_link_to_picture_field).send_keys('https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/photoSelenium.jpg')

    def click_save(self):
        self.driver.find_element(*self.click_save_button).click()

    def check_save_is_enabled(self):
        return self.driver.find_element(*self.click_save_button).is_enabled()

    def add_new_place(self, email, password, name, picture):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button()
        self.click_add_place_button()
        self.setname(name)
        self.set_link_to_picture(picture)
        self.click_save()