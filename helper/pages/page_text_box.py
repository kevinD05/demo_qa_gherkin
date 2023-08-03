from selenium.webdriver.common.by import By

class pageTextBox(object):
    
    btn_text_box = (By.XPATH, '//span[text()="Text Box"]')
    input_full_name = (By.XPATH, '//input[@id="userName"]')
    input_email = (By.XPATH, '//input[@id="userEmail"]')
    input_current_address = (By.XPATH, '//textarea[@id="currentAddress"]')
    input_permanent_address = (By.XPATH, '//textarea[@id="permanentAddress"]')
    btn_submit = (By.XPATH, '//button[@id="submit"]')
    console_message = (By.XPATH, '//div[@id="output"]//p[@id="name"]')
    