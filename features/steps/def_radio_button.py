from behave import step
import os
from helper.pages.page_radio_button import Pageradiobutton
from helper.services.acciones_basicas import Basepage
import time

@step(u'damos click al boton "Radio button"')
def step_impl(context):
    Basepage.click_button(context, Pageradiobutton.btn_radio_button)
    time.sleep(10)

@step(u'daremos click en el boton "yes"')
def step_impl(context):
    Basepage.click_button(context, Pageradiobutton.btn_yes)
    time.sleep(2)


@step(u'daremos click en el boton "Impressive"')
def step_impl(context):
    Basepage.click_button(context, Pageradiobutton.btn_impressive)
    time.sleep(2)



@step(u'Validamos que al dar click en los botones estos se muestren en el mensaje de la consola')
def step_impl(context):
    Basepage.click_button(context, Pageradiobutton.consol)

