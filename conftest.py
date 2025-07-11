import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.order_page import OrderPage
from pages.arenda_page import ArendaPage
from pages.faq_block import FAQBlock

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def base_page(driver):
    url = 'https://qa-scooter.praktikum-services.ru/'
    driver.get(url)
    page = BasePage(driver)
    return page

@pytest.fixture
def order_page(driver):
    url = 'https://qa-scooter.praktikum-services.ru/'
    driver.get(url)
    page = OrderPage(driver)
    return page

@pytest.fixture
def arenda_page(driver):
    url = 'https://qa-scooter.praktikum-services.ru/'
    driver.get(url)
    page = ArendaPage(driver)
    return page

@pytest.fixture
def fill_common_order_form(order_page, arenda_page):
    def _fill():
        order_page.click_and_fill_name_field("Имя")
        order_page.click_and_fill_surname_field("Фамилия")
        order_page.click_and_fill_adress_field("Адрес 1")
        order_page.click_and_fill_metro_field()
        order_page.click_and_fill_telephone_field("79000000000")
        order_page.click_dalee_button()

        arenda_page.click_and_fill_date_button()
        arenda_page.click_and_choose_arenda_date()
        arenda_page.click_and_choose_color_samokat()
        arenda_page.field_the_fill_comment()
        arenda_page.click_zakazat_button()
    return _fill

@pytest.fixture
def faq_block(driver):
    url = 'https://qa-scooter.praktikum-services.ru/'
    driver.get(url)
    return FAQBlock(driver)
