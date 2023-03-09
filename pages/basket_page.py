from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_dont_have_product(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "basket_have_product"

    def basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), \
            "dont have message basket is empty"
        
