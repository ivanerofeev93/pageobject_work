from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators:
    ITEM_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    ITEM_PRICE = (By.XPATH, '//p[@class="price_color"]')
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    ITEM_ADDED_ALERT = (By.CLASS_NAME, 'alert-success')
    ITEM_ADDED_NAME = (By.XPATH, '//div[1]/div[@class="alertinner "]/strong')
    BASKET_SUM_ALERT = (By.CLASS_NAME, 'alert-info')
    BASKET_SUM_PRICE = (By.XPATH, '//div[3]/div[@class="alertinner "]/p/strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, '//a[@class="btn btn-default"]')


class BasketPageLocators():
    BASKET_MESSAGE = (By.XPATH, '//*[@id="content_inner"]/p')
    CHECKOUT_BUTTON = (By.XPATH, '//*[@class="btn btn-lg btn-primary btn-block"]')