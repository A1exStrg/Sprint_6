import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage

class FAQBlock(BasePage):
    @allure.step("Кликаем по вопросу с индексом {index}")
    def click_question_by_index(self, index: int):
        self.wait.until(EC.invisibility_of_element_located(BasePageLocators.overlay))
        button_locator = BasePageLocators.faq_question(index)
        self.click(button_locator)

    @allure.step("Получаем текст ответа на вопрос с индексом {index}")
    def get_text_by_question(self, index: int):
        text_locator = BasePageLocators.faq_answer(index)
        text_elem = self.wait.until(EC.visibility_of_element_located(text_locator))
        return text_elem.text.replace('\n', ' ').strip()
