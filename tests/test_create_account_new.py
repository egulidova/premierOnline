from playwright.sync_api import Page
 
from pages.home_page import HomePage

from pages.register_page import RegisterPage
 
 
def test_check_create_account(page: Page):
    register_page = RegisterPage(page)

    page.goto(RegisterPage.URL)
    register_page.verify_page()
    register_page.fill_registration_form(RegisterPage.USER)
    register_page.click_continue()
    register_page.verify_profile_page()

def test_check_wrong_registration(page:Page):
    register_page = RegisterPage(page)

    page.goto(RegisterPage.URL)
    register_page.verify_page()
    register_page.fill_registration_form_wrong(RegisterPage.USER_WRONG)
    register_page.click_continue()
    register_page.verify_profile_page_wrong()
 
    # home = HomePage(page)

    # register = RegisterPage(page)
 
    # home.open()

    # home.verify_home_page()

    # home.click_create_account()
 
    # register.verify_page()
 
    # register.fill_email("test123@test123.com")

    # register.fill_first_name("John")

    # register.fill_last_name("Smith")

    # register.fill_password("Password123")

    # register.fill_repeat_password("Password123")
 
    # register.click_continue()

    # register.verify_profile_page()
 
    # user = {
    # "email": "test123@test123.com",
    # "first_name": "John",
    # "last_name": "Smith",
    # "password": "Password123"
    # }
 
    # register.register(user)
 