from selenium.webdriver.common.by import By

class pagepracticeforms(object):

    btn_forms = (By.XPATH, '//h5[text()="Forms"]')
    btn_practice_fomr = (By.XPATH, '//span[text()="Practice Form"]')
    input_name = (By.XPATH, '//*[@id="firstName"]')
    input_last_name = (By.XPATH, '//*[@id="lastName"]')
    input_email = (By.XPATH, '//*[@id="userEmail"]')
    input_mobil = (By.XPATH, '//*[@id="userNumber"]')
    input_Subjects = (By.XPATH, '//*[@id="subjectsContainer"]/div/div[1]')
    input_Current_Address = (By.XPATH, '//*[@id="currentAddress"]')
    btn_hobbies = (By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[1]/label')
    btn_gender = (By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]/label')
    btn_date = (By.XPATH, '//*[@id="dateOfBirthInput"]')
    fecha = (By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[7]')
    btn_state = (By.XPATH, '//*[@id="stateCity-wrapper"]/div[2]')
    ncr = (By.XPATH, '//*[@id="state"]/div/div[1]/div[1]')
    btn_city =(By.XPATH, '//*[@id="stateCity-wrapper"]/div[3]')
    delhi = (By.XPATH, '//*[@id="city"]/div/div[1]/div[1]')
