from selenium.webdriver.common.by import By

class linksbuttons(object):

    btn_links = (By.XPATH, '//*[@id="item-5"]')
    links_click = [
        (By.XPATH, '//*[@id="simpleLink"]'),
        (By.XPATH, '//*[@id="dynamicLink"]'),
        (By.XPATH, '//*[@id="created"]'),
        (By.XPATH, '//*[@id="no-content"]'),
        (By.XPATH, '//*[@id="moved"]'),
        (By.XPATH, '//*[@id="bad-request"]'),
        (By.XPATH, '//*[@id="unauthorized"]'),
        (By.XPATH, '//*[@id="forbidden"]'),
        (By.XPATH, '//*[@id="invalid-url"]')

    ]
    message = (By.XPATH, '//*[@id="linkResponse"]')
