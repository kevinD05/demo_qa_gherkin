from behave import step
from helper.services.acciones_basicas import Basepage
from helper.pages.page_buttons import buttons
import time

@step(u'damos click al boton "Buttons"')
def step_impl(context):
    Basepage.click_button(context, buttons.btn_buttons)
    time.sleep(2)
    

@step(u'daremos doble click en el boton \'double click me\'')
def step_impl(context):
    Basepage.click_button(context, buttons.btn_doble_click)
    time.sleep(2)


@step(u'daremos click derecho en el boton \' right click\'')
def step_impl(context):
    Basepage.click_button(context, buttons.btn_click_derecho)
    time.sleep(2)


@step(u'daremos click en el boton \'click me\'')
def step_impl(context):
    Basepage.click_button(context, buttons.btn_click_me)
    time.sleep(2)

@step(u'Validaremos los mensaje de la consola')
def step_impl(context):
    Basepage.click_button(context, buttons.message_console)
    time.sleep(2)