from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
import time
import allure

class OrderPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.locators_order = OrderPageLocators
        self.locators_main = MainPageLocators

    @allure.step("Заполняем поле Имя")
    def click_and_fill_name_field(self):
        button_order = self.driver.find_element(*self.locators_main.order_button)
        button_order.click()
        element = self.driver.find_element(*self.locators_order.name_field)
        element.click()
        element.send_keys('Вася')

    @allure.step("Заполняем поле фамилия")
    def click_and_fill_surname_field(self):
        element = self.driver.find_element(*self.locators_order.surname_field)
        element.click()
        element.send_keys('Волк')
        time.sleep(2)

    @allure.step("Заполняем поле адрес")
    def click_and_fill_adress_field(self):
        element = self.driver.find_element(*self.locators_order.adress_field)
        element.click()
        element.send_keys('Москва')

    @allure.step("Заполняем поле станция метро")
    def click_and_fill_metro_field(self):
        element = self.driver.find_element(*self.locators_order.metro_field)
        element.click()
        metro_station = self.driver.find_element(*self.locators_order.CHERKIZOVSKAYA_station)
        metro_station.click()

    @allure.step("Заполняем поле телефон")
    def click_and_fill_telephone_field(self):
        phone_number = '89224345566'
        element = self.driver.find_element(*self.locators_order.telephone_field)
        element.click()
        element.send_keys(phone_number)

    @allure.step("Нажимаем кнопку Далее")
    def click_dalee_button(self):
        element = self.driver.find_element(*self.locators_order.dalee_button)
        element.click()





