from behave import step
import time
import os
from helper.services.acciones_basicas import Basepage
from helper.pages.page_data_picker import pagepicker 
import time


@step(u'damos click al boton \'data picker\'')
def step_impl(context):
    Basepage.click_button(context, pagepicker.btn_data_picker)
    time.sleep(2)

@step(u'damos click en el campo \'select date\'')
def step_impl(context):
    Basepage.click_button(context, pagepicker.btn_select)
    time.sleep(2)

@step(u'seleccionamos la fecha \'08/18/2023\'')
def step_impl(context):
    Basepage.click_button(context, pagepicker.fecha)
    time.sleep(2)

@step(u'damos click en el campo \'date and time\'')
def step_impl(context):
    Basepage.click_button(context, pagepicker.btn_date_time)
    time.sleep(2)

@step(u'seleccionamos la fecha y hora \'August 18, 2023 11:30 PM\'')
def step_impl(context):
    Basepage.click_button(context, pagepicker.fecha2)
    time.sleep(2)
    Basepage.click_button(context, pagepicker.time)

@step(u'Validamos que al seleccionar una hora y fecha se refleje en los campos correspodiente')
def step_impl(context):
    pass