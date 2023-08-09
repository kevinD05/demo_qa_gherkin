from behave import step
from helper.services.acciones_basicas import Basepage
from helper.pages.page_alerts import pagealert
import time


@step(u'damos click al boton \'Alerts\'')
def step_impl(context):
    Basepage.click_button(context, pagealert.btn_alets)

@step(u'damos click en el boton \'click button to see alert\'')
def step_impl(context):
    Basepage.click_button(context, pagealert.btn_see_alert)
    time.sleep(2)

@step(u'damos click en el boton \'alert will appear after 5 seconds\'')
def step_impl(context):
    Basepage.click_button(context, pagealert.btn_after)
    time.sleep(5)

@step(u'damos click en el boton \'confirm box will appear\'')
def step_impl(context):
    Basepage.click_button(context, pagealert.btn_confirm)
    time.sleep(1)

@step(u'damos click en el boton \'prompt box will appear\'')
def step_impl(context):
    Basepage.click_button(context, pagealert.btn_prompt)
    time.sleep(2)

@step(u'Validamos que al dar click en los botones surgan las alertas correspondiente')
def step_impl(context):
    pass