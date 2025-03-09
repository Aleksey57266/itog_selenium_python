from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_IN_URL = "login"


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket") # кнопка добавить в корзину
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1") # Название товара из h1
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong") # название товара из уведомления
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color") # ищем цену твоара на странице продукта
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "div.alert-info strong") # цена товара из уведомления
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-safe.alert-noicon") # уведомление, успешного добавления в корзину
