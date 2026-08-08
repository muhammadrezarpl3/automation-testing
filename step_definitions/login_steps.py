import random

from pytest_bdd import given, when, then
from pages.login_page import LoginPage
from utils.login_data import load_users

@given("I am on the login page")
def open_login_page(page):
    login_page = LoginPage(page)
    login_page.open()

@when("I enter valid credentials")
def enter_valid_credentials(page):
    login_page = LoginPage(page)
    users = load_users()
    user = random.choice(users)
    login_page.enter_username(user["email"])
    login_page.enter_password(user["password"])

@when("I click the login button")
def click_login_button(page):
    login_page = LoginPage(page)
    login_page.click_login()

@then("I should see the dashboard")
def verify_dashboard(page):
    login_page = LoginPage(page)
    assert login_page.is_logged_in()






# @when("I enter valid credentials")
# def enter_valid_credentials(page):
#     login_page = LoginPage(page)
#     login_page.enter_username("rexperiment@gmail.com")
#     login_page.enter_password("Reza_030903")