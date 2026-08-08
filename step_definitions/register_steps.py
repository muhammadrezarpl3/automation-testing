from pytest_bdd import given, when, then

from pages.register_page import RegisterPage
from utils.test_data import generate_user


@given("I am on the registration page")
def open_registration_page(page):
    register_page = RegisterPage(page)
    register_page.open()

@when("I register with dynamically generated user data")
def register_dynamic_user(page):
    register_page = RegisterPage(page)
    user = generate_user()
    register_page.register_user(user)

@then("I should see the registration success message")
def verify_registration_success(page):
    register_page = RegisterPage(page)
    assert register_page.is_registration_successful()