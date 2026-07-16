import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.premieronline.com/"


@pytest.fixture
def home_page(page):
    page.goto(BASE_URL)
    return page

def test_open_create_account_page(page: Page):
    page.goto("https://www.premieronline.com/action/register")
    expect(page).to_have_url("https://www.premieronline.com/action/register")

def test_check_create_account(home_page, page):
    home_page.locator("a[href='https://www.premieronline.com/action/register']").click()
    expect(page).to_have_url("https://www.premieronline.com/action/register")
    email = page.locator("#email")
    expect(email).to_be_visible()
    expect(email).to_have_attribute("type", "email")
    first_name = page.locator("#first_name")
    expect(first_name).to_be_visible()
    expect(first_name).to_have_attribute("placeholder", "First Name")
    last_name = page.locator("#last_name")
    expect(last_name).to_be_visible()
    expect(last_name).to_have_attribute("placeholder", "Last Name")
    password = page.locator("#password")
    expect(password).to_be_visible()
    expect(password).to_have_attribute("type", "password")
    repeat_password = page.locator("#password_repeat")
    expect(repeat_password).to_be_visible()
    expect(repeat_password).to_have_attribute("type", "password")
    continue_btn = page.get_by_role("button", name="Continue")
    expect(continue_btn).to_be_visible()
    expect(continue_btn).to_be_enabled()
    page.locator("#email").fill("test@test.com")
    page.locator("#first_name").fill("John")
    page.locator("#last_name").fill("Smith")
    page.locator("#password").fill("Password123")
    page.locator("#password_repeat").fill("Password123")
    expect(page.locator("#email")).to_have_value("test@test.com")
    expect(page.locator("#first_name")).to_have_value("John")
    expect(page.locator("#last_name")).to_have_value("Smith")
 