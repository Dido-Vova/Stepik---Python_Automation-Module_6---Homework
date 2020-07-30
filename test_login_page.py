import time
import random

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
    #Try register using existing email
    page.reopen()
    page.should_be_login_page()
    page.register_new_user(login, password)
    page.should_be_authorized_user()

#!!!Следующие тесты объединить в один

@pytest.mark.run
@pytest.mark.need_review_custom_scenarios
@pytest.mark.parametrize('login, password', [(str(random.randint(1, 1000000)) + "@uniquemail.org", '12345qwertASDFG'),
                                             (str(random.randint(1, 1000000)) + "@t-est1234.р-ф567890", '12345qwertASDFG'),
                                             pytest.param(str(random.randint(1, 1000000)) + "@uniquemail.org", 'Eight61!',
                                                          marks=pytest.mark.xfail),
                                             (str(random.randint(1, 1000000)) + "@uniquemail.org", 'Nine6781!')])

def test_register_new_user_using_unique_email(browser, login, password):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.register_new_user(login, password)
    page.should_be_authorized_user()