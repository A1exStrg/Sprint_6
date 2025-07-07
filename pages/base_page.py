from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        try:
            cookie_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass  # баннер не появился — ничего страшного
    #универсальный поиск
    def find(self, locator: tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

    #клик по элементу
    @allure.step("Кликаем по элементу {locator}")
    def click(self, locator: tuple):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

        # Явное ожидание, пока элемент не будет перекрыт
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

        try:
            element.click()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="click_error",
                          attachment_type=allure.attachment_type.PNG)
            raise e
    @allure.step("Вводим текст '{text}' в элемент {locator}")
    def fill(self, locator: tuple, text: str):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Кликаем по вопросу с индексом {index}")
    def click_question_by_index(self, index: int):
        overlay = (By.CLASS_NAME, "Order_Overlay__3KW-T")
        self.wait.until(EC.invisibility_of_element_located(overlay))
        button_locator = (By.ID, f"accordion__heading-{index}")
        self.driver.save_screenshot(f"screenshot_before_click_index_{index}.png")
        self.click(button_locator)

    @allure.step("Получаем текст ответа на вопрос с индексом {index}")
    def get_text_by_question(self, index: int):
        text_locator = (By.ID, f"accordion__panel-{index}")
        text_elem = self.wait.until(EC.visibility_of_element_located(text_locator))
        return text_elem.text.replace('\n', ' ').strip()

