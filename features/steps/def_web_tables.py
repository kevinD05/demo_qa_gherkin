from behave import step
from helper.services.acciones_basicas import Basepage
from helper.pages.page_web_tables import Pagewetable
from helper.services.forms import formswebtbables
import time
from selenium.webdriver.common.by import By


@step(u'damos click al boton "web tables"')
def step_impl(context):
    Basepage.click_button(context, Pagewetable.btn_web_tables)
    time.sleep(2)

@step(u'daremos click en el boton \'add\'')
def step_impl(context):
    Basepage.click_button(context, Pagewetable.add)

@step(u'ingresamos los datos del formulario del usuario')
def step_impl(context, user):
    formswebtbables(context).web_form(user)

@step(u'daremos click en el boton "submit"')
def step_impl(context):
    Basepage.click_button(context, Pagewetable.btn_submit1)

@step(u'daremos click en el espacio de busqueda')
def step_impl(context):
    Basepage.click_button(context, Pagewetable.busqueda)

@step(u'ingresamos el nombre que asignamos al guarda los datos del formulario')
def step_impl(context):
    name = context.find_element(By.XPATH, '//*[@id="searchBox"]')
    name.send_keys('Chester')
    time.sleep(2)

@step(u'daremos click en el boton editar')
def step_impl(context):
    Basepage.click_button(context, Pagewetable.editar)


@step(u'editaremos el formulario')
def step_impl(context):
    name_edit = context.find_element(By.XPATH, '//*[@id="firstName"]')
    name_edit.send_keys('kira')
    time.sleep(2)


@step(u'daremos click en el submit')
def step_impl(context):
    Basepage.click_button(context, Pagewetable.btn_submit1)


@step(u'daremos click en el boton eliminar')
def step_impl(context):
    Basepage.click_button(context, Pagewetable.eliminar)

@step(u'Validamos que se envien los datos del formulario y que tambien se editen y se eliminen')
def step_impl(context):
    pass