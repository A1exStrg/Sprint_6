import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.order_page import OrderPage
from pages.arenda_page import ArendaPage
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# @pytest.fixture
# def driver():
#     driver = webdriver.Firefox()
#     yield driver
#     driver.quit()

@pytest.fixture
def driver():
    # Укажи путь до firefox.exe и geckodriver.exe
    binary = FirefoxBinary("C:/Program Files/Mozilla Firefox/firefox.exe")
    service = Service("E:/geckodriver/geckodriver.exe")  # путь к geckodriver
    driver = webdriver.Firefox(service=service, firefox_binary=binary)
    yield driver
    driver.quit()

@pytest.fixture
def base_page(driver):
    driver.get('https://qa-scooter.praktikum-services.ru/')
    page = BasePage(driver)
    return page

@pytest.fixture
def order_page(driver):
    driver.get('https://qa-scooter.praktikum-services.ru/')
    page = OrderPage(driver)
    return page

@pytest.fixture
def arenda_page(driver):
    driver.get('https://qa-scooter.praktikum-services.ru/order')
    page = ArendaPage(driver)
    return page


