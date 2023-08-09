from selenium.webdriver.common.by import By

class Pagewetable(object):

    btn_web_tables = (By.XPATH, '//*[@id="item-3"]')
    add = (By.XPATH, '//*[@id="addNewRecordButton"]')
    input_first_name = (By.XPATH, '//*[@id="firstName"]')
    input_last_name = (By.XPATH, '//*[@id="lastName"]')
    input_email = (By.XPATH, '//*[@id="userEmail"]')
    input_age = (By.XPATH, '//*[@id="age"]')
    input_salary = (By.XPATH, '//*[@id="salary"]')
    input_department = (By.XPATH, '//*[@id="department"]')
    btn_submit1 = (By.XPATH, '//*[@id="submit"]')
    busqueda = (By.XPATH, '//*[@id="searchBox"]')
    editar = (By.XPATH, '//*[@id="edit-record-1"]/svg')
    eliminar = (By.XPATH, '//*[@id="delete-record-1"]/svg/path')
