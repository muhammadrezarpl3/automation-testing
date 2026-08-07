from pytest_bdd import given, when, then
from pages.login_page import LoginPage

@given("I am on the login page")
def open_login_page(page):
    login_page = LoginPage(page)
    login_page.open()

@when("I enter valid credentials")
def enter_valid_credentials(page):
    login_page = LoginPage(page)
    login_page.enter_username("rexperiment@gmail.com")
    login_page.enter_password("Reza_030903")

@when("I click the login button")
def click_login_button(page):
    login_page = LoginPage(page)
    login_page.click_login()

@then("I should see the dashboard")
def click_login_button(page):
    login_page = LoginPage(page)
    login_page.is_logged_in()