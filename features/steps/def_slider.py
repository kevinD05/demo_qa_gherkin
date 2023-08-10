from behave import step
import os
from helper.pages.page_slider import pageslider
from helper.services.acciones_basicas import Basepage
from helper.services.acciones_basicas import SliderHandler
import time

@step(u'damos click al boton \'slider\'')
def step_impl(context):
    Basepage.click_button(context, pageslider.slider)
    time.sleep(2)

@step(u'damos click al boton del slider')
def step_impl(context):
    Basepage.click_button(context, pageslider.btn_slider)
    time.sleep(2)

@step(u'moveremos el slider hasta le numero 100')
def step_impl(context):
    SliderHandler.drag_slider_to_position(context, pageslider.btn_slider)
    time.sleep(2)

@step(u'Validamos el numero del recuadro del slider este debe ser 100')
def step_impl(context):
    pass
