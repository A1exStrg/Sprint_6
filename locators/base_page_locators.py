from selenium.webdriver.common.by import By

class BasePageLocators:
    overlay = (By.CLASS_NAME, "Order_Overlay__3KW-T")
    cookie_button = (By.ID, "rcc-confirm-button")

    @staticmethod
    def faq_question(index: int):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def faq_answer(index: int):
        return By.ID, f"accordion__panel-{index}"