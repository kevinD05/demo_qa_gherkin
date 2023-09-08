from selenium.webdriver.common.by import By
 
class pagebrowser(object):

    btn_alerts_frame = (By.XPATH, '//h5[text()="Alerts, Frame & Windows"]')
    btn_browser = (By.XPATH, '//span[text()="Browser Windows"]')
    new_tab =  (By.XPATH, '//*[@id="tabButton"]')
    new_windows = (By.XPATH, '//*[@id="windowButton"]')
    new_windows_message = (By.XPATH, '//*[@id="messageWindowButton"]')