from behave import step
import os
from helper.pages.page_forms import pagepracticeforms
from helper.services.acciones_basicas import Basepage
from helper.services.forms import practiceform
import time

@step(u'cargue la pagina, damos click al boton "Forms"')
def step_impl(context):
    Basepage.click_button(context, pagepracticeforms.btn_forms)
    context.browser.execute_script('window.scrollTo(0, 300)')
    time.sleep(2)

@step(u'damos click al boton \'practice forms\'')
def step_impl(context):
    Basepage.click_button(context, pagepracticeforms.btn_practice_fomr)
    context.browser.execute_script('window.scrollTo(0, 300)')


@step(u'ingresamos los datos del formulario del usuario \'<forms>\'')
def step_impl(context):
    pass

@step(u'damos click en boton de genero "Male"')
def step_impl(context):
    pass

@step(u'damos click en el boton hobbies "sports"')
def step_impl(context):
    pass

@step(u'damos click en el campo date of birth "5/8/23"')
def step_impl(context):
    pass
    
@step(u'damos click en el campo select state seleccionamos \'Ncr\'')
def step_impl(context):
  pass

@step(u'damos click en el campo select city seleccionamos \'delhi\'')
def step_impl(context):
    pass