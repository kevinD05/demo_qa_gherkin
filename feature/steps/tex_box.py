from behave import step
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

def create_driver():
    return webdriver.Chrome()

def get_driver(context):
    if not hasattr(context, "browser") or context.browser is None:
        context.browser = create_driver()
    return context.browser

@step(u'ingresamos a la url')
def step_impl(context):
    driver = get_driver(context)
    driver.get("https://demoqa.com/elements")

@step(u'cargue la pagina, damos click al boton text box')
def step_impl(context):
    driver = get_driver(context)
    btn_text_box = driver.find_element(By.XPATH, '//*[@id="item-0"]/span')
    btn_text_box.click()
    time.sleep(3)

@step(u'validar que nos mande el formulario de la text box')
def step_impl(context):
    time.sleep(2)


@step(u'que estoy en la página de registro')
def step_impl(context):
    time.sleep(1)


@step(u'ingresar full name "usuario123"')
def step_impl(context):
    driver = get_driver(context)
    name = driver.find_element(By.XPATH, '//*[@id="userName"]')
    name.send_keys('usuario123')
    time.sleep(2)


@step(u'ingresar email "usuario@example.com"')
def step_impl(context):
    driver = get_driver(context)
    email = driver.find_element(By.XPATH, '//*[@id="userEmail"]')
    email.send_keys('usuario@example.com')
    time.sleep(2)

@step(u'ingresar current addres')
def step_impl(context):
    driver = get_driver(context)
    current = driver.find_element(By.XPATH, '//*[@id="currentAddress"]')
    current.send_keys('direccion 12345')
    time.sleep(2)

@step(u'ingresar permanet addres')
def step_impl(context):
    driver = get_driver(context)
    permanet = driver.find_element(By.XPATH, '//*[@id="permanentAddress"]')
    permanet.send_keys('direccion 12345')
    time.sleep(2)

@step(u'dar clic en el boton submit')
def step_impl(context):
    driver = get_driver(context)
    button =  driver.find_element(By.XPATH, '//*[@id="submit"]')
    button.click()
    time.sleep(4)


@step(u'esperar que todo se haya aguardado')
def step_impl(context):
    time.sleep(5)