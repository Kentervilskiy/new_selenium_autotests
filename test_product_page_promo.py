import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('par', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])

def test_add_to_cart(browser, par):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{par}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()