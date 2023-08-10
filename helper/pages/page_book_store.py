from selenium.webdriver.common.by import By

class pagebookstore(object):

    btn_book_store = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[6]/span/div/div[1]')
    book_store = (By.XPATH, '//*[@id="item-2"]/span')
    username = (By.XPATH, '//*[@id="userName"]')
    password = (By.XPATH, '//*[@id="password"]')
    login = (By.XPATH, '//*[@id="login"]')
    book1 = (By.XPATH, '//*[@id="see-book-Git Pocket Guide"]/a')
    btn_add = (By.XPATH, '//*[@id="addNewRecordButton"]')
    book2 = (By.XPATH, '//*[@id="see-book-Designing Evolvable Web APIs with ASP.NET"]/a')
    