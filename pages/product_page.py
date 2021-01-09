from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_add_correct_item(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_ADDED_ALERT), "'Item added' alert is not presented"
        product_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        product_name_in_alert = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_NAME).text
        assert product_name in product_name_in_alert, "No product name in the message"

    def sum_of_basket_should_match_the_item(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_SUM_ALERT), "'Basket sum' alert is not presented"
        price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        price_in_alert = self.browser.find_element(*ProductPageLocators.BASKET_SUM_ALERT).text
        assert price in price_in_alert, "Prices are not equal"