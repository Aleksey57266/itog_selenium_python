from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert LoginPageLocators.LOGIN_IN_URL in self.browser.current_url, "в url нет login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Отсутствует форма логина"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Отсутствует форма регистрации"

    def register_new_user(self, email, password):
        register_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        register_email.send_keys(email)
        register_password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        register_password1.send_keys(password)
        register_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        register_password2.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BTN_REGISTRATION)
        button_register.click()
