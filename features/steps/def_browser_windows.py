from behave import step
import os
from helper.pages.page_browser_windows import pagebrowser 
from helper.services.acciones_basicas import Basepage
import time

@step(u'cargue la pagina, damos click al boton "Alerts, Frame & Windows"')
def step_impl(context):
    Basepage.click_button(context, pagebrowser.btn_alerts_frame)
    context.browser.execute_script('window.scrollTo(0, 500)')
    time.sleep(2)

@step(u'damos click al boton \'Browser Windows\'')
def step_impl(context):
    Basepage.click_button(context, pagebrowser.btn_browser)
    time.sleep(2)


@step(u'damos click en el boton \'New tab\'')
def step_impl(context):
    Basepage.click_button(context, pagebrowser.new_tab)
    time.sleep(2)


@step(u'damos click en el boton \'new windows\'')
def step_impl(context):
    Basepage.click_button(context, pagebrowser.new_windows)
    time.sleep(2)


@step(u'damos click en el boton \'New windows message\'')
def step_impl(context):
    Basepage.click_button(context, pagebrowser.new_windows_message)
    time.sleep(2)


@step(u'Validamos que al darle click en los botones seamos rediccionadosa una nueva ventana')
def step_impl(context):
    pass