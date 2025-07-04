from selenium.webdriver.common.by import By

class MainPageLocators:
    order_button = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")