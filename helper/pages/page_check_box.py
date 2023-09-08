from selenium.webdriver.common.by import By

class Pagecheckbox(object):
     
     btn_check_box = (By.XPATH, '//*[@id="item-1"]')
     btn_mas = (By.XPATH, '//button[@class="rct-option rct-option-expand-all"]')
     rct_checkbox = (By.XPATH, '//span[@class="rct-checkbox"]')
     btn_menos = (By.XPATH, '//button[@class="rct-option rct-option-collapse-all"]')
     message = (By.XPATH, '//*[@id="result"]')