from dotenv import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from webdriver_manager.chrome import ChromeDriverManager

def environment_load(context):
    load_dotenv()
    config = dotenv_values(find_dotenv())
    for key, value in config.items():
        setattr(context, key, value)

def before_all(context):
    environment_load(context)

    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    # Agregar otras opciones si es necesario

    # Elimina el uso de ChromeDriverManager() y pasa solo las opciones
    context.browser = webdriver.Chrome(options=chrome_options)

    print("Se esta ejecutando la prueba con selenium")


def after_all(context):
    print("Se ejecuto Correctamente la prueba!")


def before_tag(context, tag):
    pass


def after_tag(context, tag):
    pass


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    pass


def before_step(context, step):
    pass


def after_step(context, step):
    pass