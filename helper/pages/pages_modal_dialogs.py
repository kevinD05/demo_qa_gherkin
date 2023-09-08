from selenium.webdriver.common.by import By

class pagemodaldialogs(object):

    btn_modal = (By.XPATH, '//span[text()="Modal Dialogs"]')
    btn_small = (By.XPATH, '//button[@id="showSmallModal"]')
    close_small = (By.XPATH, '//button[@id="closeSmallModal"]')
    btn_large = (By.XPATH, '//*[@id="showLargeModal"]')
    close_large = (By.XPATH, '//button[@id="closeLargeModal]')
    