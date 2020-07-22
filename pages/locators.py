from selenium.webdriver.common.by import By

class BasePageLocators ():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, "span>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGOUT_LINK = (By.ID, "logout_link")


class MainPageLocators():
    EMPTY_TEMP = None

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_FORM_EMAIL_FIELD = (By.ID, 'id_registration-email')
    REGISTER_FORM_PASSWORD_FIELD = (By.ID, 'id_registration-password1')
    REGISTER_FORM_REPEAT_PASSWORD_FIELD = (By.ID, 'id_registration-password2')
    REGISTER_FORM_SUBMIT_BTN = (By.NAME, 'registration_submit')
    ERROR_MESSAGE_SIGN = (By.CSS_SELECTOR, "#register_form .icon-exclamation-sign")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADDED_TO_BASKET_NOTIFICATION = (By.XPATH, "//div[@id='messages']/div[contains(@class,'alert-success')]")
    PRODUCT_NAME = (By.XPATH, "//div[@id='content_inner']//div/h1")
    PRODUCT_NAME_NOTIFICATION = (By.XPATH, "//div[@id='messages']//div/strong")
    BASKET_TOTAL_PRICE_NOTIFICATION = (By.XPATH, "//div[@id='messages']/div[contains(@class,'alert-info')]")
    PRODUCT_PRICE = (By.XPATH, "//div[@id='content_inner']//div/p")
    TOTAL_BASKET_PRICE = (By.XPATH, "//div[@id='messages']//div/p/strong")

class BasketPageLocators():
    LIST_OF_PURCHASES = (By.ID, "basket_formset")
    BASKET_IS_EMPTY_NOTIFICATION = (By.CSS_SELECTOR, "#content_inner>p")
