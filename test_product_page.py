from .pages.product_page import ProductPage
import pytest

#@pytest.mark.parametrize('offer', ["?promo=offer0",
#                                  "?promo=offer1",
#                                  "?promo=offer2",
#                                  "?promo=offer3",
#                                  "?promo=offer4",
#                                  "?promo=offer6",
#                                  pytest.param("?promo=offer7", marks=pytest.mark.xfail),
#                                  "?promo=offer8",
#                                  "?promo=offer9"])
#def test_guest_can_add_product_to_basket(browser, offer):
#    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{offer}"
#    page = ProductPage(browser, link)
#    page.open()
#    page.should_add_to_basket()
#    page.solve_quiz_and_get_code()
#    page.should_add_correct_item()
#    page.sum_of_basket_should_match_the_item()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_basket()
    page.success_message_should_dessapear()

