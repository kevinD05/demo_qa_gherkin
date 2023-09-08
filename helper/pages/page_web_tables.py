from selenium.webdriver.common.by import By

class Pagewetable(object):

    btn_web_tables = (By.XPATH, '//*[@id="item-3"]')
    add = (By.XPATH, '//*[@id="addNewRecordButton"]')
    input_first_name = (By.XPATH, '//input[@id="firstName"]')
    input_last_name = (By.XPATH, '//input[@id="lastName"]')
    input_email = (By.XPATH, '//input[@id="userEmail"]')
    input_age = (By.XPATH, '//input[@id="age"]')
    input_salary = (By.XPATH, '//input[@id="salary"]')
    input_department = (By.XPATH, '//input[@id="department"]')
    btn_submit1 = (By.XPATH, '//button[@id="submit"]')
    busqueda = (By.XPATH, '//input[@id="searchBox"]')
    editar = (By.XPATH, '//span[@id="edit-record-1"]')
    eliminar = (By.XPATH, '//span[@id="delete-record-1"]')
