from helper.services.acciones_basicas import Basepage
from helper.pages.page_text_box import pageTextBox
from helper import usuarios
import time

class formsDemoQA(Basepage):

    def select_user(self, user):

        if user == 'Kevin':
            return usuarios.KEVIN
        elif user == 'Luis':
            return usuarios.LUIS
        else:
            print("El usuario no existe")


    def fill_form(self, user):

        self.browser.find_element(*pageTextBox.input_full_name).send_keys(self.select_user(user)['fullname'])
        self.browser.find_element(*pageTextBox.input_email).send_keys(self.select_user(user)['email'])
        self.browser.find_element(*pageTextBox.input_current_address).send_keys(self.select_user(user)['currentAddress'])
        self.browser.find_element(*pageTextBox.input_permanent_address).send_keys(self.select_user(user)['permanentAddress'])
        