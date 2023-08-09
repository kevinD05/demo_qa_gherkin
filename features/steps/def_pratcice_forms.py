from behave import step
import os
from helper.pages.page_forms import pagepracticeforms
from helper.services.acciones_basicas import Basepage
from helper.services.forms import practiceform
import time

@step(u'cargue la pagina, damos click al boton "Forms"')
def step_impl(context):
    Basepage.click_button(context, pagepracticeforms.btn_forms)
    time.sleep(2)

@step(u'damos click al boton \'practice forms\'')
def step_impl(context):
    Basepage.click_button(context, pagepracticeforms.btn_practice_fomr)

@step(u'ingresamos los datos del formulario del usuario \'<forms>\'')
def step_impl(context,user):
    practiceform(context).pratice_form(user)

@step(u'damos click en boton de genero "Male"')
def step_impl(context):
    Basepage.click_button(context, pagepracticeforms.btn_gender)
    time.sleep(2)

@step(u'damos click en el boton hobbies "sports"')
def step_impl(context):
    Basepage.click_button(context, pagepracticeforms.btn_hobbies)
    time.sleep(2)

@step(u'damos click en el campo date of birth "5/8/23"')
def step_impl(context):
    Basepage.click_button(context, pagepracticeforms.btn_date)
    time.sleep(2)
    Basepage.click_button(context, pagepracticeforms.fecha)
    
@step(u'damos click en el campo select state seleccionamos \'Ncr\'')
def step_impl(context):
    Basepage.click_button(context, pagepracticeforms.btn_state)
    time.sleep(2)
    Basepage.click_button(context, pagepracticeforms.ncr)

@step(u'damos click en el campo select city seleccionamos \'delhi\'')
def step_impl(context):
    Basepage.click_button(context, pagepracticeforms.btn_city)
    time.sleep(2)
    Basepage.click_button(context, pagepracticeforms.delhi)