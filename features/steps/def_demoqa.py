from behave import step
import time
import os
from helper.services.acciones_basicas import Basepage
from helper.pages.page_demoqa import pageDemoqa
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@step(u'Ingresamos a la url "URL_QA"')
def step_impl(context):
    url = os.getenv('URL_QA')
    context.browser.get(url)

@step(u'cargue la pagina, damos click al boton "Elements"')
def step_impl(context):
    Basepage.esperarMostrarElemento(context, pageDemoqa.btn_elements)
    Basepage.click_button(context, pageDemoqa.btn_elements)
    time.sleep(3)

@step(u'validos que nos mande a las opcions de elementos')
def step_impl(context):
    elemento = context.browser.find_element(*pageDemoqa.btn_text_box).is_displayed()
    assert elemento, "El elemento no existe"

