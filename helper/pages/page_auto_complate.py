from selenium.webdriver.common.by import By

class pageautocomplate(object):

    btn_widgets = (By.XPATH, '//h5[text()="Widgets"]')
    btn_auto = (By.XPATH, '//span[text()="Auto Complete"]')
    btn_multiple = (By.XPATH, '//*[@id="autoCompleteMultipleContainer"]/div/div[1]')
    