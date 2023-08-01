import time

class Basepage():
    
    def __init__(self, context):
        self.browser = context.browser

    def click_button(self, element):
        time.sleep(3)
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
