from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket_btn_click(self):
        self.should_be_btn_add_to_basket()
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket.click()

    def should_be_added_product_to_basket(self):
        self.should_be_notification_added_to_basket()
        self.should_be_the_same_product_name_in_notification()
        self.should_be_notification_with_cart_price()
        self.should_be_the_same_product_price_in_notification()

    def should_be_btn_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), \
            "no 'add to basket' button at the product page"

    def should_be_notification_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET_NOTIFICATION), \
            "no notification that product added to the basket"

    def should_be_the_same_product_name_in_notification(self):  # Название товара в сообщении должно совпадать \
        # с тем товаром, который вы действительно добавили
        assert self.is_value_match_expectation(*ProductPageLocators.PRODUCT_NAME, \
                                               *ProductPageLocators.PRODUCT_NAME_NOTIFICATION), \
            "product name in notification not fitted with added product"

    def should_be_notification_with_cart_price(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_PRICE_NOTIFICATION), \
            "no notification with total price of the basket"

    def should_be_the_same_product_price_in_notification(self):  # Стоимость корзины совпадает с ценой товара
        assert self.is_value_match_expectation(*ProductPageLocators.PRODUCT_PRICE, \
                                               *ProductPageLocators.TOTAL_BASKET_PRICE), \
            "product price in notification not fitted with added product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_NOTIFICATION), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_BASKET_NOTIFICATION), \
            "Success message didn't disappeared within specified time"
