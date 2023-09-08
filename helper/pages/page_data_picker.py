from selenium.webdriver.common.by import By

class pagepicker(object):

    btn_data_picker = (By.XPATH, '//span[text()="Date Picker"]')
    btn_select = (By.XPATH, '//*[@id="datePickerMonthYearInput"]')
    fecha = (By.XPATH, '//*[@id="datePickerMonthYear"]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[6]')
    btn_date_time = (By.XPATH, '//*[@id="dateAndTimePickerInput"]')
    time = (By.XPATH, '//*[@id="dateAndTimePicker"]/div[2]/div[2]/div/div/div[3]/div[2]/div/ul/li[47]')
    fecha2 = (By.XPATH, '//*[@id="dateAndTimePicker"]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[6]')
