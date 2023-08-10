from behave import step
from helper.services.acciones_basicas import Basepage
from helper.pages.page_book_store import pagebookstore
import time
from selenium.webdriver.common.by import By



@step(u'cargue la pagina, damos click al boton "book store application"')
def step_impl(context):
    Basepage.click_button(context, pagebookstore.btn_book_store)
    time.sleep(2)

@step(u'damos click al boton \'book store\'')
def step_impl(context):
    Basepage.click_button(context, pagebookstore.btn_store)
    time.sleep(2)

@step(u'ingresamos el user y password correspondiente \'<user>\'')
def step_impl(context):
    login = context.find_element(By.XPATH, '//*[@id="login"]')
    login.click()
    username = context.find_element(By.XPATH, '//*[@id="userName"]')
    username.click()
    username.send_keys('aaaaaa')
    password = context.find_element(By.XPATH, '//*[@id="password"]')
    password.click()
    password.send_keys('Alaputaestacontra5556%')
    time.sleep(2)


@step(u'damos click al libro con el nombre \' Working Introduction\'')
def step_impl(context):
    Basepage.click_button(context, pagebookstore.book1)

@step(u'damos click al boton \'add to your collection\'')
def step_impl(context):
    Basepage.click_button(context, pagebookstore.btn_add)

@step(u'damos click al libro con el nombre \'Harnessing the Power of the Web\'')
def step_impl(context):
    Basepage.click_button(context, pagebookstore.book2)

@step(u'damos click al boton \'add to your collection\'')
def step_impl(context):
    Basepage.click_button(context, pagebookstore.btn_add)

@step(u'Validamos que los libros se guarden en nuestro perfil')
def step_impl(context):
    pass