import allure
import pytest
from data.faq_data import index_question
from data.order_test_data import order_test_cases

@pytest.mark.parametrize("index, expected", index_question)
@allure.title("Проверка текста ответа на вопрос №{index}")
@allure.description("Проверяет, что при клике по вопросу в блоке FAQ отображается корректный ответ.")
def test_questions(base_page, index, expected):
    base_page.click_question_by_index(index)
    actual_text = base_page.get_text_by_question(index)
    assert actual_text == expected

@pytest.mark.parametrize("data", order_test_cases)
def test_order_from_different_buttons(order_page, arenda_page, data):
    # Клик по нужной кнопке "Заказать"
    if data["button"] == "top":
        order_page.click_top_order_button()
    else:
        order_page.click_bottom_order_button()

    # Заполнение формы заказа
    order_page.click_and_fill_name_field(data["name"])
    order_page.click_and_fill_surname_field(data["surname"])
    order_page.click_and_fill_adress_field(data["address"])
    order_page.click_and_fill_metro_field()
    order_page.click_and_fill_telephone_field(data["phone"])
    order_page.click_dalee_button()

    # Заполнение формы аренды
    arenda_page.click_and_fill_date_button()
    arenda_page.click_and_choose_arenda_date()
    arenda_page.click_and_choose_color_samokat()
    arenda_page.field_the_fill_comment()
    arenda_page.click_zakazat_button()

    # ✅ Сохраняем текст подтверждения и проверяем
    confirmation_text = arenda_page.click_yes_order_field()
    assert "Заказ оформлен" in confirmation_text

    # ✅ Проверяем редирект
    url = arenda_page.click_samokat_button()
    assert "dzen.ru" in url

