from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        self.should_be_basket_url()
        self.should_be_empty_basket_notification()
        self.should_be_empty_purchased_items_form()

    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, \
            "Current URL doesn't contain word 'basket'"

    def should_be_empty_basket_notification(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_NOTIFICATION), \
            "No notification, that basket is empty"

    def should_be_empty_purchased_items_form(self):
        assert self.is_not_element_present(*BasketPageLocators.LIST_OF_PURCHASES), \
            "Basket is not empty"
