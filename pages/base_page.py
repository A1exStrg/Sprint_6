from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Кликаем по вопросу с индексом {index}")
    def click_question_by_index(self, index: int):
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "Order_Overlay__3KW-T")))
        button_locator = (By.ID, f"accordion__heading-{index}")
        button = self.wait.until(EC.element_to_be_clickable(button_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        button.click()

    @allure.step("Получаем текст ответа на вопрос с индексом {index}")
    def get_text_by_question(self, index: int):
        text_locator = (By.ID, f"accordion__panel-{index}")
        text_element = self.wait.until(EC.visibility_of_element_located(text_locator))
        return text_element.text.replace('\n', ' ').strip()

