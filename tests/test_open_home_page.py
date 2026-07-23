import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage

BASE_URL = "https://www.premieronline.com/"

@pytest.fixture
def home_page(page):
    page.goto(BASE_URL)
    return page

@pytest.mark.parametrize("name, href", HomePage.MENU_ITEMS)

def test_navigation_menu(home_page, name, href):
    
    link = home_page.get_by_role("link", name=name, exact=True)
 
    expect(link).to_be_visible()
    expect(link).to_have_attribute("href", href)

def test_open_home_page(home_page):

    expect(home_page).to_have_url("https://www.premieronline.com/")
    expect(home_page).to_have_title(
        "Premier Online - leading provider of online event registration for sports events"
        )

def test_check_logo(home_page):

    logo = home_page.get_by_alt_text("Premiere Online")
    expect(logo).to_be_visible()
    expect(logo).to_have_attribute("alt", "Premiere Online")

    logo_link = home_page.locator("a.uk-logo")
    expect(logo_link).to_have_attribute("href", "https://www.premieronline.com")

def test_check_sign_in(home_page):

    sign_in_button = home_page.locator("a[href='https://www.premieronline.com/action/dologin']").first 
    expect(sign_in_button).to_be_visible()
    expect(sign_in_button).to_have_attribute("href","https://www.premieronline.com/action/dologin")

# def test_check_menu_events(home_page):
    
#     events_link = home_page.get_by_text("Events").nth(0)
#     expect(events_link).to_be_visible()
#     expect(events_link).to_have_attribute("href", href)

# def test_check_menu_ratings(home_page):
    
#     ratings_link = home_page.get_by_text("Ratings").nth(0)
#     expect(ratings_link).to_be_visible()
#     expect(ratings_link).to_have_attribute("href", "https://www.premieronline.com/event_ratings.php")

# def test_check_menu_help(home_page):
    
#     help_link = home_page.get_by_text("Help").nth(0)
#     expect(help_link).to_be_visible()
#     expect(help_link).to_have_attribute("href", "https://www.premieronline.com/help")

# def test_check_menu_lang(home_page):
    
#     lang_link = home_page.get_by_text("عربى").nth(0)
#     expect(lang_link).to_be_visible()
#     expect(lang_link).to_have_attribute("href", "https://www.premieronline.com/action/lang.php?lang=ar")