from behave import step
import time
import os
from helper.services.acciones_bacicas import Basepage
from helper.pages.pages_demoqa import pageDemoqa
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@step(u'Ingresamos a la url "URL_QA"')
def step_impl(context):
    url = os.getenv('URL_QA')
    context.browser.get(url)
    time.sleep(5)

@step(u'cargue la pagina, damos click al boton "Elements"')
def step_impl(context):
    # Esperar hasta que el botón "Elements" esté presente y sea clickeable
    elements_button = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(pageDemoqa.btn_elements)
    )
    # Mover el cursor fuera del área del botón "Elements"
    actions = ActionChains(context.browser)
    actions.move_to_element_with_offset(elements_button, -10, -10)
    actions.perform()
    # Hacer clic en el botón "Elements" usando JavaScript
    context.browser.execute_script("arguments[0].click();", elements_button)
    time.sleep(3)

@step(u'validos que nos mande a las opcions de elementos')
def step_impl(context):
    elemento = context.browser.find_element(*pageDemoqa.btn_text_box).is_displayed()
    assert elemento, "El elemento no existe"

