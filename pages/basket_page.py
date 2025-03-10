from .base_page import BasePage
from .locators import CartLocators


class BasketPage(BasePage):
    def checking_the_availability_of_items_in_the_cart(self):
        assert self.is_not_element_present(*CartLocators.PRODUCT_IN_CART), "Товары есть"

    def check_for_empty_cart_text(self):
        assert self.is_element_present(*CartLocators.EMPTY_CART_TEXT), "Нет текста о пустой корзине"
