from selenium.webdriver.support.wait import WebDriverWait
from locators.arenda_page_locators import ArendaPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure

class ArendaPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.locators_arenda = ArendaPageLocators()

    @allure.step("Заполняем поле дата")
    def click_and_fill_date_button(self):
        date = '03.07.2025'
        button = self.wait.until(EC.element_to_be_clickable(self.locators_arenda.date_button))
        button.clear()
        button.send_keys(date)
        button.send_keys(Keys.ENTER)

    @allure.step("Заполняем поле срок аренды")
    def click_and_choose_arenda_date(self):
        element = self.driver.find_element(*self.locators_arenda.arenda_date)
        element.click()
        element_date = self.driver.find_element(*self.locators_arenda.choose_drop_down_value)
        element_date.click()

    @allure.step("Выбираем чек-бокс цвет самоката")
    def click_and_choose_color_samokat(self):
        element = self.driver.find_element(*self.locators_arenda.color_samokat_button)
        element.click()

    @allure.step("Заполняем поле комментарий для курьера")
    def field_the_fill_comment(self):
        element = self.driver.find_element(*self.locators_arenda.comment_for_button)
        element.send_keys('no comment')

    @allure.step("Кликаем кнопку Заказать")
    def click_zakazat_button(self):
        element = self.driver.find_element(*self.locators_arenda.zakazat_button)
        element.click()

    @allure.step("Оформляем заказ -ДА проверяем оформление заказа")
    def click_yes_order_field(self):
        element_yes = self.driver.find_element(*self.locators_arenda.agree_yes_button)
        element_yes.click()
        order_is_ready = self.wait.until(EC.visibility_of_element_located(self.locators_arenda.order_is_ready_field))
        text_order = order_is_ready.text
        assert 'Заказ оформлен' in text_order
        element_stat_order = self.driver.find_element(*self.locators_arenda.status_order)
        element_stat_order.click()

    @allure.step("Проверка клика логотипа самокат и яндекс")
    def click_samokat_button(self):
        self.wait.until(EC.invisibility_of_element_located(self.locators_arenda.wait_button))
        element = self.wait.until(EC.element_to_be_clickable(self.locators_arenda.samokat_button))
        element.click()
        self.wait.until(EC.url_to_be("https://qa-scooter.praktikum-services.ru/"))
        current_url = self.driver.current_url
        assert current_url == "https://qa-scooter.praktikum-services.ru/"
        element = self.wait.until(EC.element_to_be_clickable(self.locators_arenda.logo_yandex_button))
        element.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(EC.url_to_be("https://dzen.ru/?yredirect=true"))
        assert "dzen.ru" in self.driver.current_url












