from behave import step
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from helper.services.acciones_basicas import Basepage
from helper.pages.page_text_box import pageTextBox
from helper.services.forms import formsDemoQA


@step(u'damos click al boton "Text Box"')
def step_impl(context):
    Basepage.click_button(context, pageTextBox.btn_text_box)


@step(u'ingresamos los datos del formulario del usuario "{user}"')
def step_impl(context, user):
    formsDemoQA(context).fill_form(user)
    time.sleep(3)


@step(u'validamos que se envien los datos del formulario correctamente')
def step_impl(context):
    Basepage.click_button(context, pageTextBox.btn_submit)

    mensaje_consola = Basepage.validarElementoExistente(context, pageTextBox.console_message)

    assert mensaje_consola == True, 'No se envio el formulario'