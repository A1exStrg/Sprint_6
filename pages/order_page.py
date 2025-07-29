from locators.order_page_locators import OrderPageLocators
import allure
from .base_page import BasePage

class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    @allure.step("Кликаем верхнюю кнопку Заказать")
    def click_top_order_button(self):
        self.click(self.locators.order_button_top)

    @allure.step("Кликаем нижнюю кнопку Заказать")
    def click_bottom_order_button(self):
        self.click(self.locators.order_button_bottom)

    @allure.step("Заполняем поле Имя")
    def click_and_fill_name_field(self, name: str = "Вася"):
        self.fill(self.locators.name_field, name)

    @allure.step("Заполняем поле Фамилия")
    def click_and_fill_surname_field(self, surname: str = "Иванов"):
        self.fill(self.locators.surname_field, surname)

    @allure.step("Заполняем поле Адрес")
    def click_and_fill_adress_field(self, address: str = "Москва, ул. Пушкина, д. 1"):
        self.fill(self.locators.adress_field, address)

    @allure.step("Выбираем станцию метро")
    def click_and_fill_metro_field(self):
        self.click(self.locators.metro_field)
        self.click(self.locators.CHERKIZOVSKAYA_station)

    @allure.step("Заполняем поле Телефон")
    def click_and_fill_telephone_field(self, phone: str = "+79991112233"):
        self.fill(self.locators.telephone_field, phone)

    @allure.step("Нажимаем кнопку Далее")
    def click_dalee_button(self):
        self.click(self.locators.dalee_button)



