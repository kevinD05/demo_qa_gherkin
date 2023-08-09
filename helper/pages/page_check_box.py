from selenium.webdriver.common.by import By

class Pagecheckbox(object):
     
     btn_check_box = (By.XPATH, '//span[text()="Checke Box"]')
     btn_mas = (By.XPATH, '//*[@id="tree-node"]/div/button[1]/svg')
     rct_checkbox = (By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/span[1]')
     btn_menos = (By.XPATH, '//*[@id="tree-node"]/div/button[2]/svg')
     message = (By.XPATH, '//*[@id="result"]')