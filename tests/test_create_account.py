#import pytest
from playwright.sync_api import Page, expect

# BASE_URL = "https://www.premieronline.com/"


# @pytest.fixture
# def home_page(page):
#     page.goto(BASE_URL)
#     return page

def test_check_create_account(page:Page):
    
    page.goto("https://www.premieronline.com/")
    expect(page).to_have_url("https://www.premieronline.com/")
    expect(page).to_have_title("Premier Online - leading provider of online event registration for sports events")
    page.get_by_role("button", name="Create Account").click()
    #page.locator("a[href='https://www.premieronline.com/action/register']").first().click()
    
    expect(page).to_have_url("https://www.premieronline.com/action/register")
    email = page.locator("#email")
    expect(email).to_be_visible()
    expect(email).to_have_attribute("type", "email")
    page.locator("#email").fill("test123@test123.com")
    expect(page.locator("#email")).to_have_value("test123@test123.com")

    first_name = page.locator("#first_name")
    expect(first_name).to_be_visible()
    expect(first_name).to_have_attribute("placeholder", "First Name")
    page.locator("#first_name").fill("John")
    expect(page.locator("#first_name")).to_have_value("John")

    last_name = page.locator("#last_name")
    expect(last_name).to_be_visible()
    expect(last_name).to_have_attribute("placeholder", "Last Name")
    page.locator("#last_name").fill("Smith")
    expect(page.locator("#last_name")).to_have_value("Smith")

    password = page.locator("#password")
    expect(password).to_be_visible()
    expect(password).to_have_attribute("type", "password")
    page.locator("#password").fill("Password123")
    
    repeat_password = page.locator("#password_repeat")
    expect(repeat_password).to_be_visible()
    expect(repeat_password).to_have_attribute("type", "password")
    page.locator("#password_repeat").fill("Password123")
    
    continue_btn = page.get_by_role("button", name="Continue")
    expect(continue_btn).to_be_visible()
    expect(continue_btn).to_be_enabled()
    continue_btn.click()

    expect(page).to_have_url("https://www.premieronline.com/create_profile.php")
       
     