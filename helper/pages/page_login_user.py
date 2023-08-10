from selenium.webdriver.common.by import By

class pagelogin(object):
     btn_book_store = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[6]/span/div/div[1]')
     btn_login = (By.XPATH, '//*[@id="item-0"]/span')
     new_user = (By.XPATH, '//*[@id="newUser"]')
     fisrt_name = (By.XPATH, '//*[@id="firstname"]')
     last_name = (By.XPATH, '//*[@id="lastname"]')
     user_name = (By.XPATH, '//*[@id="userName"]')
     password = (By.XPATH, '//*[@id="password"]')
     btn_register = (By.XPATH, '//*[@id="register"]')