import time
import pytest

from .pages.login_page import LoginPage


def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


@pytest.mark.need_review_custom_scenarios
@pytest.mark.xfail
def test_register_new_user_using_existing_email(browser):
    #Preconditions. Creating a new user.
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    login = str(time.time()) + "@uniquemail.org"
    password = "12345qwertASDFG"
    page.register_new_user(login, password)
    page.should_be_authorized_user()
    # browser.quit() #почему-то после этой команды не могу открывать страницу заново,
    # появляется ошибка Failed to establish a new connection: [WinError 10061] Подключение не установлено
    # , т.к. конечный компьютер отверг запрос на подключение')). Разобраться
    page.click_the_logout_button()
    #Try register using existing email
    browser.get(link)
    page.should_be_login_page()
    page.register_new_user(login, password)
    page.should_be_authorized_user()

#!!!Следующие тесты объединить в один

@pytest.mark.need_review_custom_scenarios
def test_register_new_user_using_unique_email(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    login = str(time.time()) + "@uniquemail.org"
    password = "12345qwertASDFG"
    page.register_new_user(login, password)
    page.should_be_authorized_user()

@pytest.mark.need_review_custom_scenarios
def test_register_new_user_using_special_characters_in_email_domain_name(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    login = str(time.time()) + "@t-est1234.р-ф567890"
    password = "12345qwertASDFG"
    page.register_new_user(login, password)
    page.should_be_authorized_user()


@pytest.mark.need_review_custom_scenarios
@pytest.mark.xfail
def test_register_new_user_using_password_with_8_characters(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    login = str(time.time()) + "@uniquemail.org"
    password = "Eight61!"
    page.register_new_user(login, password)
    page.should_be_authorized_user()


@pytest.mark.need_review_custom_scenarios
def test_register_new_user_using_password_with_9_characters(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    login = str(time.time()) + "@uniquemail.org"
    password = "Eight671!"
    page.register_new_user(login, password)
    page.should_be_authorized_user()


