from behave import step
import os
from helper.pages.pages_dynamic import pagedynamic
from helper.services.acciones_basicas import Basepage
import time

@step(u'damos click al boton "Dynamic properties"')
def step_impl(context):
    Basepage.click_button(context, pagedynamic.btn_dynamic)


@step(u'damos click al boton "color change"')
def step_impl(context):
    Basepage.click_button(context, pagedynamic.btn_change_color)

@step(u'esperaremos 5 segundos hasta que el boton \'will enable 5 seconds" sea visible y daremos click')
def step_impl(context):
    Basepage.click_button(context, pagedynamic.btn_enable)

@step(u'damos click en el boton "visible after 5 seconds" despues de 5 segundos')
def step_impl(context):
    Basepage.click_button(context, pagedynamic.btn_after)

@step(u'Validamos que al dar click en los botones el cortono cambie')
def step_impl(context):
    pass