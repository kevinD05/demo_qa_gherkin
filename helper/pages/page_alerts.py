from selenium.webdriver.common.by import By

class pagealert(object):

    btn_alets = (By.XPATH, '//*[@id="item-1"]')
    btn_see_alert = (By.XPATH, '//*[@id="alertButton"]')
    btn_after = (By.XPATH, '//*[@id="timerAlertButton"]')
    btn_confirm = (By.XPATH, '//*[@id="confirmButton"]')
    btn_prompt = (By.XPATH, '//*[@id="promtButton"]')