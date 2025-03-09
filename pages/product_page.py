from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON) # ищем кнопку "добавить в корзину"
        add_to_basket_button.click()  # нажимаем кнопку
        self.solve_quiz_and_get_code() # решаем уравнение и отправляем в алерт

    def should_be_product_added_to_basket_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text # ищем название товара в H1
        message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE).text # ищем название товара в уведомлении
        assert product_name in message, f"Expected '{product_name}' to be in '{message}'" # сравниваем

    def should_be_basket_total_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text # ищем цену твоара на странице продукта
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text # цена товара из уведомления
        assert product_price in basket_total, f"Expected '{product_price}' to be in '{basket_total}'" # сравниваем

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успешном выполнении отображается, но его не должно быть"

    def should_success_message_propal(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успешном выполнении отображается и не пропало"
