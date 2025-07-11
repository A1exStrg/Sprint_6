import allure
import pytest
from data.faq_data import index_question


@allure.epic("FAQ")
@allure.feature("Проверка ответов на вопросы")
class TestFAQBlock:

    @pytest.mark.parametrize("index, expected", index_question)
    @allure.title("Проверка текста ответа на вопрос №{index}")
    @allure.description("Проверяет, что при клике по вопросу в блоке FAQ отображается корректный ответ.")
    def test_questions(self, faq_block, index, expected):
        faq_block.click_question_by_index(index)
        actual_text = faq_block.get_text_by_question(index)
        assert actual_text == expected


@allure.epic("Оформление заказа")
@allure.feature("Кнопки 'Заказать'")
class TestOrderFromButtons:

    @allure.title("Оформление заказа через верхнюю кнопку")
    def test_order_from_top_button(self, order_page, fill_common_order_form, arenda_page):
        order_page.click_top_order_button()
        fill_common_order_form()

        confirmation_text = arenda_page.click_yes_order_field()
        assert "Заказ оформлен" in confirmation_text

    @allure.title("Оформление заказа через нижнюю кнопку")
    def test_order_from_bottom_button(self, order_page, fill_common_order_form, arenda_page):
        order_page.click_bottom_order_button()
        fill_common_order_form()

        confirmation_text = arenda_page.click_yes_order_field()
        assert "Заказ оформлен" in confirmation_text


@allure.epic("Оформление заказа")
@allure.feature("Редирект после заказа")
class TestOrderRedirect:

    @allure.title("Редирект на Dzen после успешного заказа")
    def test_redirect_to_dzen_after_order(self, order_page, fill_common_order_form, arenda_page):
        order_page.click_top_order_button()
        fill_common_order_form()
        arenda_page.click_yes_order_field()

        url = arenda_page.click_samokat_button()
        assert "dzen.ru" in url
