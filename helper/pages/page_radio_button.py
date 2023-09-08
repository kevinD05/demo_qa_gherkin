from selenium.webdriver.common.by import By

class Pageradiobutton(object):

    btn_radio_button = (By.XPATH, '//*[@id="item-2"]/span')
    btn_yes = (By.XPATH, '//label[@for="yesRadio"]')
    btn_impressive = (By.XPATH, '//label[@for="impressiveRadio"]')
    consol = (By.XPATH, '//span[@class="text-success"]')