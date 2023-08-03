import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basepage():
    
    def __init__(self, context):
        self.browser = context.browser

    def click_button(self, element):
        
        WebDriverWait(self.browser, 10).until(
        EC.element_to_be_clickable(element))

        try:
            elemento = self.browser.find_element(*element)
            elemento.click()
        except:
            print("El elemento no existe")


    def fill_input(self, element, value):
        try:
            elemento = self.browser.find_element(*element)
            elemento.send_keys(value)
        except:
            print()

    def validarElementoExistente(self, element):
        
        try:
            elemento = self.browser.find_element(*element)
            return True
        except:
            return False
        

    def esperarMostrarElemento(self, element):
        # Esperar hasta que el botón "Elements" esté presente y sea clickeable

        WebDriverWait(self.browser, 10).until(
        EC.element_to_be_clickable(element)
    )
