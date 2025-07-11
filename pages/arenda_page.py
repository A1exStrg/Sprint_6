from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import allure
from .base_page import BasePage
from locators.arenda_page_locators import ArendaPageLocators

class ArendaPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ArendaPageLocators()

    @allure.step("Заполняем поле даты аренды")
    def click_and_fill_date_button(self, date: str = '03.07.2025'):
        element = self.wait.until(EC.element_to_be_clickable(self.locators.date_button))
        element.clear()
        element.send_keys(date)
        element.send_keys(Keys.ENTER)

    @allure.step("Выбираем срок аренды")
    def click_and_choose_arenda_date(self):
        self.click(self.locators.arenda_date)
        self.click(self.locators.choose_drop_down_value)

    @allure.step("Выбираем цвет самоката")
    def click_and_choose_color_samokat(self):
        self.click(self.locators.color_samokat_button)

    @allure.step("Заполняем поле комментарий")
    def field_the_fill_comment(self, comment: str = "no comment"):
        self.fill(self.locators.comment_for_button, comment)

    @allure.step("Нажимаем кнопку 'Заказать'")
    def click_zakazat_button(self):
        self.click(self.locators.zakazat_button)

    @allure.step("Подтверждаем заказ и проверяем оформление")
    def click_yes_order_field(self):
        self.click(self.locators.agree_yes_button)
        order_ready = self.wait.until(EC.visibility_of_element_located(self.locators.order_is_ready_field))
        text = order_ready.text
        self.click(self.locators.status_order)
        return text

    @allure.step("Проверка перехода на главную и на Яндекс.Дзен")
    def click_samokat_button(self):
        self.wait.until(EC.invisibility_of_element_located(self.locators.wait_button))
        self.click(self.locators.samokat_button)

        self.wait.until(EC.url_to_be("https://qa-scooter.praktikum-services.ru/"))
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"

        self.click(self.locators.logo_yandex_button)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        self.wait.until(EC.url_to_be("https://dzen.ru/?yredirect=true"))
        return self.driver.current_url
