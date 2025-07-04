from selenium.webdriver.common.by import By
class ArendaPageLocators:

    date_button = (By.XPATH, "//input[@placeholder = '* Когда привезти самокат']")
    arenda_date = (By.CLASS_NAME, "Dropdown-control")
    choose_drop_down_value = (By.XPATH, "//div[text() = 'сутки']")
    color_samokat_button = (By.ID, "black")
    comment_for_button = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    zakazat_button = (By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать'])[2]")
    agree_yes_button = (By.XPATH, "//button[text()= 'Да']")
    #order_is_ready_field = (By.XPATH, "//div[text()= 'Заказ оформлен']")
    order_is_ready_field = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text()= 'Заказ оформлен']")
    status_order = (By.XPATH, "//button[text()='Посмотреть статус']")
    samokat_button = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    logo_yandex_button = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    wait_button = (By.CLASS_NAME,"Order_Overlay__3KW-T")

