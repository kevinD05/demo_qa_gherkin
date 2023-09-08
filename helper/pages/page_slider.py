from selenium.webdriver.common.by import By

class pageslider(object):
    
   slider = (By.XPATH, '//span[text()="Slider"]')
   btn_slider = (By.XPATH, '//*[@id="sliderContainer"]/div[1]/span/div')
   recuadro = (By.XPATH, '//*[@id="sliderValue"]')
