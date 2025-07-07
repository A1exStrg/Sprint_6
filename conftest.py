import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.order_page import OrderPage
from pages.arenda_page import ArendaPage

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


