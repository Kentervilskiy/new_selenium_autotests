from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "add to cart button is not presented"

    def add_product_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_cart_button.click()
    def should_be_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        text_product_name = product_name.text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        text_success_message = success_message.text
        price_in_catalog = self.browser.find_element(*ProductPageLocators.PRICE_IN_CATALOG)
        text_price_in_catalog = price_in_catalog.text
        price_in_success_massage = self.browser.find_element(*ProductPageLocators.PRICE_IN_SUCCESS_MESSAGE)
        text_price_in_success_massage = price_in_success_massage.text
        assert text_product_name == text_success_message
        assert text_price_in_catalog == text_price_in_success_massage
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)