from behave import step
import os
from helper.pages.page_login_user import pagelogin
from helper.services.acciones_basicas import Basepage
from helper.services.forms import login_user 
import time


@step(u'cargue la pagina, damos click al boton "book store"')
def step_impl(context):
    Basepage.click_button(context, pagelogin.btn_book_store)
    time.sleep(2)

@step(u'damos click al boton \'login\'')
def step_impl(context):
    Basepage.click_button(context, pagelogin.btn_login)
    time.sleep(2)

@step(u'damos click al boton \'new user\'')
def step_impl(context):
    Basepage.click_button(context, pagelogin.new_user)
    time.sleep(2)

@step(u'ingresamos los datos del formalario \'<login>\'')
def step_impl(context, user):
    login_user(context).login(user)
    time.sleep(2)

@step(u'damos click al boton registrar')
def step_impl(context):
    Basepage.click_button(context, pagelogin.btn_register)
    time.sleep(2)


@step(u'validamos que usuario este ingresado')
def step_impl(context):
    pass