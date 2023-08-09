from selenium.webdriver.common.by import By

class pagemodaldialogs(object):

    btn_modal = (By.XPATH, '//*[@id="item-4"]/span')
    btn_small = (By.XPATH, '//*[@id="showSmallModal"]')
    close_small = (By.XPATH, '//*[@id="closeSmallModal"]')
    btn_large = (By.XPATH, '//*[@id="showLargeModal"]')
    close_large = (By.XPATH, '//*[@id="closeLargeModal"]')
    