from behave import step
from helper.services.acciones_basicas import Basepage
from helper.pages.page_web_tables import Pagewetable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium import *

@step(u'damos click al boton "web tables"')
def step_impl(context):
    Basepage.click_button(context, Pagewetable.btn_web_tables)
    time.sleep(2)

@step(u'daremos click en el boton \'add\'')
def step_impl(context):
    Basepage.click_button(context, Pagewetable.add)
    time.sleep(2)

@step(u'ingresamos los datos del formulario del usuario')
def step_impl(context):
    driver = context.browser
   
    first_name = driver.find_element(By.XPATH, '//input[@id="firstName"]')
    last_name = driver.find_element(By.XPATH, '//input[@id="lastName"]')
    email = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
    age = driver.find_element(By.XPATH, '//input[@id="age"]')
    salary = driver.find_element(By.XPATH, '//input[@id="salary"]')
    department = driver.find_element(By.XPATH, '//input[@id="department"]')
    first_name.send_keys('chester')
    last_name.send_keys('diaz')
    email.send_keys('kd1931@gmail.com')
    age.send_keys('22')
    salary.send_keys('500')
    department.send_keys('testing')
    time.sleep(2)

@step(u'daremos click en el boton "submit"')
def step_impl(context):
    Basepage.click_button(context, Pagewetable.btn_submit1)
    time.sleep(2)

@step(u'daremos click en el espacio de busqueda')
def step_impl(context):
    Basepage.click_button(context, Pagewetable.busqueda)
    time.sleep(2)

@step(u'ingresamos el nombre que asignamos al guarda los datos del formulario')
def step_impl(context):
    driver = context.browser
    name = driver.find_element(By.XPATH, '//*[@id="searchBox"]')
    name.send_keys('Chester')
    time.sleep(2)

@step(u'daremos click en el boton editar')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="edit-record-1"]/svg'))
    )
    
    Basepage.click_button(context, Pagewetable.editar)
    
    time.sleep(2)

@step(u'editaremos el formulario')
def step_impl(context):
    driver = context.browser
    name_edit = driver.find_element(By.XPATH, '//*[@id="firstName"]')
    name_edit.send_keys('chester')
    time.sleep(2)

@step(u'daremos click en el submit')
def step_impl(context):
    Basepage.click_button(context, Pagewetable.btn_submit1)
    time.sleep(2)

@step(u'daremos click en el boton eliminar')
def step_impl(context):
    Basepage.click_button(context, Pagewetable.eliminar)
    time.sleep(1)

@step(u'Validamos que se envien los datos del formulario y que tambien se editen y se eliminen')
def step_impl(context):
    pass