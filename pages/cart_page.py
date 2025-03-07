from .base_page import BasePage
from .locators import ProductPageLocators


class CartPage(BasePage):
    def click_button_add_to_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button_add_to_cart.click()
