from behave import step
import time
from selenium.webdriver.common.by import By
import os
from helper.services.acciones_basicas import Basepage
from helper.pages.page_auto_complate import pageautocomplate
import time


@step(u'cargue la pagina, damos click al boton "Widgets"')
def step_impl(context):
    Basepage.click_button(context, pageautocomplate.btn_widgets)
    time.sleep(2)


@step(u'damos click al boton \'Auto Complete\'')
def step_impl(context):
    Basepage.click_button(context, pageautocomplate.btn_auto)
    time.sleep(2)


@step(u'damos click en el campo multiple color')
def step_impl(context):
    multiple = context.find_element(By.XPATH, '//*[@id="autoCompleteMultipleContainer"]/div')
    multiple.click()
    time.sleep(1)


@step(u'escribiremos dos nombre de un color \'yellow\',\'red\'')
def step_impl(context):
    multiple = context.find_element(By.XPATH, '//*[@id="autoCompleteMultipleContainer"]/div')
    multiple.send_keys('yellow')
    multiple.click()
    multiple.send_keys('red')
    multiple.click()
    time.sleep(2)



@step(u'damos click en el campo single color')
def step_impl(context):
    single = context.find_element(By.XPATH, '//*[@id="autoCompleteSingleContainer"]/div/div[1]')
    single.click()
    time.sleep(2)


@step(u'escribiremos un nombre de un color \'blue\'')
def step_impl(context):
    single = context.find_element(By.XPATH, '//*[@id="autoCompleteSingleContainer"]/div/div[1]')
    single.click()
    time.sleep(2)
    single.send_keys('blue')


@step(u'Validamos que al escribir nombres de colores se auto complete')
def step_impl(context):
    pass