from playwright.sync_api import Page, expect
 
 
class HomePage:
 
    URL = "https://www.premieronline.com/"

    MENU_ITEMS = [
        ("Events", "https://www.premieronline.com/calendar"),
        ("Ratings", "https://www.premieronline.com/event_ratings.php"),
        ("Help", "https://www.premieronline.com/help"),
        ("عربى", "https://www.premieronline.com/action/lang.php?lang=ar"),
    ]
 
    def __init__(self, page: Page):

        self.page = page

        self.create_account_btn = page.get_by_role(

            "button",

            name="Create Account"

        )
 
    def open(self):

        self.page.goto(self.URL)
 
    def verify_home_page(self):

        expect(self.page).to_have_url(self.URL)

        expect(self.page).to_have_title(

            "Premier Online - leading provider of online event registration for sports events"

        )
 
    def click_create_account(self):

        self.create_account_btn.click()
 