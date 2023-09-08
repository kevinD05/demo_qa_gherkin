from behave import step
import os
from helper.pages.page_link import linksbuttons
from helper.services.acciones_basicas import Basepage
import time

@step(u'damos click al boton "Links"')
def step_impl(context):
    Basepage.click_button(context, linksbuttons.btn_links)
    time.sleep(2)


@step(u'daremos click a todos los links')
def step_impl(context):
    Basepage.click_multiple_links(context, linksbuttons.btn_links)
    time.sleep(2)


@step(u'Validaremos el mensaje de la consola despues de a ver dado click en los links')
def step_impl(context):
    Basepage.click_button(context, linksbuttons.message)