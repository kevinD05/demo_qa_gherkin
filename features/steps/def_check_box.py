from behave import step
import time
import os
from helper.services.acciones_basicas import Basepage
from helper.pages.page_check_box import Pagecheckbox
import time

@step(u'damos click al boton "check box"')
def step_impl(context):
    Basepage.click_button(context, Pagecheckbox.btn_check_box)
    

@step(u'damos clic en boton "+"')
def step_impl(context):
    Basepage.click_button(context, Pagecheckbox.btn_mas)

@step(u'damos click a las check box')
def step_impl(context):
    Basepage.click_button(context, Pagecheckbox.rct_checkbox)

@step(u'damos clic en el boton "-"')
def step_impl(context):
    Basepage.click_button(context, Pagecheckbox.btn_menos)

@step(u'Validamos que al dar click en las check box estas se muestren seleccionadas')
def step_impl(context):
    Basepage.click_button(context, Pagecheckbox.message)

    mensaje_confimacion = Basepage.validarElementoExistente(context, Pagecheckbox.message)

    assert mensaje_confimacion == True, 'No se seleccionaron las check boxes'