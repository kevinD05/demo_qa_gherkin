from behave import step
import os
import time
from helper.services.acciones_basicas import Basepage
from helper.pages.page_element import PageDemoQA


@step(u'Ingresamos a la url "URL_QA"')
def step_impl(context):
    url = os.getenv('URL_QA')
    context.browser.get(url)
    time.sleep(3)
    context.browser.execute_script('window.scrollTo(0, 430)')
    time.sleep(1)


@step(u'cargue la pagina, damos click al boton "Elements"')
def step_impl(context):
    Basepage.click_button(context, PageDemoQA.btn_elements)
    context.browser.execute_script('window.scrollTo(0, 420)')
    time.sleep(3)

@step(u'validos que nos mande a las opcions de elementos')
def step_impl(context):
    elemento = Basepage.validarElementoExistente(context, PageDemoQA.btn_text_box)
    assert elemento == True, "El elemento no existe"
