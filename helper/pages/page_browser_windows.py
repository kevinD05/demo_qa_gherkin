from selenium.webdriver.common.by import By
 
class pagebrowser(object):

    btn_alerts_frame = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[3]/span/div/div[1]')
    btn_browser = (By.XPATH, '//*[@id="item-0"]/span')
    new_tab =  (By.XPATH, '//*[@id="tabButton"]')
    new_windows = (By.XPATH, '//*[@id="windowButton"]')
    new_windows_message = (By.XPATH, '//*[@id="messageWindowButton"]')