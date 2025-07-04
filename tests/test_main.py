import time
from pages.base_page import BasePage
from pages.order_page import OrderPage
from pages.arenda_page import ArendaPage
import allure
import pytest

index_question = [
    (0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
    (1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
    (2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
    (3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
    (4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
    (5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
    (6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
    (7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
]

@pytest.mark.parametrize("index, expected", index_question)
@allure.title("Проверка текста ответа на вопрос №{index}")
@allure.description("Проверяет, что при клике по вопросу в блоке FAQ отображается корректный ответ.")
def test_questions(base_page, index, expected):
    base_page.click_question_by_index(index)
    actual_text = base_page.get_text_by_question(index)
    assert actual_text == expected

@allure.title("Тестирование заказа и перехода на страницу яндекса и дзена")
def test_order(order_page, arenda_page):
    order_page.click_and_fill_name_field() #клик и заполнение поля Имя
    order_page.click_and_fill_surname_field()
    order_page.click_and_fill_adress_field()
    order_page.click_and_fill_metro_field()
    order_page.click_and_fill_telephone_field()
    order_page.click_dalee_button()
    arenda_page.click_and_fill_date_button()
    arenda_page.click_and_choose_arenda_date()
    arenda_page.click_and_choose_color_samokat()
    arenda_page.field_the_fill_comment()
    arenda_page.click_zakazat_button()
    arenda_page.click_yes_order_field()
    arenda_page.click_samokat_button()

    time.sleep(5)

# def test_arenda(arenda_page):
#     arenda_page.click_and_fill_date_button()
#
#     time.sleep(3)


