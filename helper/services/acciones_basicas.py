import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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
    
    def double_click_button(self, element):
        try:
            elemento = self.browser.find_element(*element)
            action_chains = ActionChains(self.browser)
            action_chains.double_click(elemento).perform()
        except:
            print("El elemento no existe")

    def right_click_button(self, element):
        try:
            elemento = self.browser.find_element(*element)
            action_chains = ActionChains(self.browser)
            action_chains.context_click(elemento).perform()
        except:
            print("El elemento no existe")
    
    def click_multiple_links(self, elements):
        for element in elements:
            try:
                link = self.browser.find_element(*element)
                link.click()
            except:
                print(f"El elemento {element} no existe")

    def click_button_and_return(self, element):
        try:
            self.ventana_principal = self.browser.current_window_handle
            
            elemento = self.browser.find_element(*element)
            elemento.click()

            time.sleep(2)

            for ventana in self.browser.window_handles:
                if ventana != self.ventana_principal:
                    self.browser.switch_to.window(ventana)
                    break

           
            self.browser.switch_to.window(self.ventana_principal)
        except:
            print("El elemento no existe o hubo un problema al manejar ventanas")

class SliderHandler:
    def __init__(self, driver):
        self.driver = driver

    def drag_slider_to_position(self, slider_selector, position_percentage):
        self.driver.get('https://demoqa.com/slider')
        slider = self.driver.find_element (By.XPATH, '//*[@id="sliderContainer"]/div[1]/span/div')
        slider_width = slider.size['width']
        action_chains = ActionChains(self.driver)
        desired_position = slider_width * (position_percentage / 100)
        action_chains.click_and_hold(slider).move_by_offset(desired_position, 0).release().perform()

