from .pages.product_page import ProductPage
import pytest
import time


@pytest.mark.parametrize('offer', ["?promo=offer0",
                                  "?promo=offer1",
                                  "?promo=offer2",
                                  "?promo=offer3",
                                  "?promo=offer4",
                                  "?promo=offer6",
                                  "?promo=offer7",
                                  "?promo=offer8",
                                  "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{offer}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_add_correct_item()
    page.sum_of_basket_should_match_the_item()





