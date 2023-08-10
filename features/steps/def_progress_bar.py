from behave import step
import os
from helper.pages.page_progress_bar import pageprogressbar 
from helper.services.acciones_basicas import Basepage
import time


@step(u'damos click al boton \'Progress Bar\'')
def step_impl(context):
    Basepage.click_button(context, pageprogressbar.btn_progress)

@step(u'damos click en el boton \'star\'')
def step_impl(context):
    Basepage.click_button(context, pageprogressbar.star)
    time.sleep(8)

@step(u'esperemos que la barra de progresso llegue ala mitad y damos click en el boton \'stop\'')
def step_impl(context):
    Basepage.click_button(context, pageprogressbar.star)


@step(u'Validamos que la barra de progresso este %50')
def step_impl(context):
    pass