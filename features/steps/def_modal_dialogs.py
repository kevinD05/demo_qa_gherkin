from behave import step
import os
from selenium.webdriver.common.by import By
from helper.pages.pages_modal_dialogs import pagemodaldialogs
from helper.services.acciones_basicas import Basepage
import time


@step(u'damos click al boton \'modal dialogs\'')
def step_impl(context):
    Basepage.click_button(context, pagemodaldialogs.btn_modal)
    time.sleep(2)

@step(u'damos click en el boton \'small modal\'')
def step_impl(context):
    Basepage.click_button(context, pagemodaldialogs.btn_small)
    time.sleep(2)

@step(u'cerraremos la alerta emergente')
def step_impl(context):
    Basepage.click_button(context, pagemodaldialogs.close_small)

@step(u'damos click en el click \'Large modal\'')
def step_impl(context):
    driver = context.browser
    Basepage.click_button(context, pagemodaldialogs.btn_large)
    time.sleep(2)

    close = driver.find_element(By.XPATH, '//button[@id="closeLargeModal]')
    close.click()


@step(u'Validamos que al dar click en los botones la alerta sea visible')
def step_impl(context):
    pass