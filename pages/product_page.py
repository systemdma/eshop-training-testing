from .base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_busket(self):
        self.browser.find_element(*ProductPageLocators.BASKET).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_name_from_basket(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BUSKET).text

    def get_price_before(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_BEFORE_CLICK).text    

    def get_price_after(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_AFTER_CLICK).text    