from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "Login link is not asserted"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_confirm_input = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_INPUT)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_input.send_keys(str(email))
        password_input.send_keys(str(password))
        password_confirm_input.send_keys(str(password))
        register_button.click()
