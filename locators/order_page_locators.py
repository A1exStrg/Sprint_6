from selenium.webdriver.common.by import By

class OrderPageLocators:
    name_field = (By.XPATH, "//input[@placeholder='* Имя']")
    surname_field = (By.XPATH, "//input[@placeholder='* Фамилия']")
    adress_field = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_field = (By.XPATH, "//input[@placeholder='* Станция метро']")
    CHERKIZOVSKAYA_station = (By.XPATH, "//div[text()='Черкизовская']")
    telephone_field = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    dalee_button = (By.XPATH, "//button[contains(., 'Далее')]")