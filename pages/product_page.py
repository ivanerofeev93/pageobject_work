from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_add_correct_item(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_ADDED_ALERT), "'Item added' box is not presented"
        product_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        product_name_in_alert = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_NAME).text
        assert product_name == product_name_in_alert, "Wrong product name in basket"

    def sum_of_basket_should_match_the_item(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_SUM_ALERT), "'Basket sum' box is not presented"
        price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        price_in_alert = self.browser.find_element(*ProductPageLocators.BASKET_SUM_PRICE).text
        assert price == price_in_alert, "Prices are not equal"