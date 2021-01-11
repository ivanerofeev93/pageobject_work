from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_BUTTON), \
            "Chekout button is presented, but should not be"

    def should_be_empty_basket_message(self):
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text
        assert "Your basket is empty" in basket_message, \
            "Message not appeared"
