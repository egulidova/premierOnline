from playwright.sync_api import Page, expect
 
 
class RegisterPage:
 
    URL = "https://www.premieronline.com/action/register"
    USER = {
        "email": "test123@test123.com",
        "first_name": "John",
        "last_name": "Smith",
        "password": "Password123"
        }
    
    USER_WRONG = {
        "email": "test123@test123com",
        "first_name": "Joh1n",
        "last_name": "S1mith",
        "password": "Password123",
        "repeat_password": "Password12"
    }
 
    def __init__(self, page: Page):

        self.page = page
 
        self.email = page.locator("#email")

        self.first_name = page.locator("#first_name")

        self.last_name = page.locator("#last_name")

        self.password = page.locator("#password")

        self.repeat_password = page.locator("#password_repeat")

        self.continue_btn = page.get_by_role("button", name="Continue")
 
    def verify_page(self):

        expect(self.page).to_have_url(self.URL)

    def fill_registration_form(self, user: dict):
        self.email.fill(user["email"])
        expect(self.email).to_be_visible()
        expect(self.email).to_have_attribute("type", "email")
        self.email.fill(user["email"])
        expect(self.email).to_have_value(user["email"])
        
        expect(self.first_name).to_be_visible()
        expect(self.first_name).to_have_attribute(
            "placeholder",
            "First Name"
        )
        self.first_name.fill(user["first_name"])
        expect(self.first_name).to_have_value(user["first_name"])
        
        expect(self.last_name).to_be_visible()
        expect(self.last_name).to_have_attribute(
            "placeholder",
            "Last Name"
        )
        self.last_name.fill(user["last_name"])
        
        expect(self.last_name).to_have_value(user["last_name"])
        expect(self.password).to_be_visible()
        expect(self.password).to_have_attribute("type", "password")
        self.password.fill(user["password"])

        expect(self.repeat_password).to_be_visible()
        expect(self.repeat_password).to_have_attribute("type", "password")
        self.repeat_password.fill(user["password"])
 
    def fill_registration_form_wrong(self, user_wrong: dict):
        self.email.fill(user_wrong["email"])
        expect(self.email).to_be_visible()
        expect(self.email).to_have_attribute("type", "email")
        self.email.fill(user_wrong["email"])
        expect(self.email).to_have_value(user_wrong["email"])
        
        expect(self.first_name).to_be_visible()
        expect(self.first_name).to_have_attribute(
            "placeholder",
            "First Name"
        )
        self.first_name.fill(user_wrong["first_name"])
        expect(self.first_name).to_have_value(user_wrong["first_name"])
        
        expect(self.last_name).to_be_visible()
        expect(self.last_name).to_have_attribute(
            "placeholder",
            "Last Name"
        )
        self.last_name.fill(user_wrong["last_name"])
        
        expect(self.last_name).to_have_value(user_wrong["last_name"])
        expect(self.password).to_be_visible()
        expect(self.password).to_have_attribute("type", "password")
        self.password.fill(user_wrong["password"])

        expect(self.repeat_password).to_be_visible()
        expect(self.repeat_password).to_have_attribute("type", "password")
        self.repeat_password.fill(user_wrong["repeat_password"])

    def click_continue(self):

        expect(self.continue_btn).to_be_visible()

        expect(self.continue_btn).to_be_enabled()

        self.continue_btn.click()
 
    def verify_profile_page(self):

        expect(self.page).to_have_url(

            "https://www.premieronline.com/create_profile.php"

        )
    def verify_profile_page_wrong(self):

        expect(self.page).to_have_url(

            "https://www.premieronline.com/create_profile.php"

        )
        error_msg = self.page.get_by_text('Error:')
        expect(error_msg).to_be_visible


    # def fill_email(self, email: str):

    #     expect(self.email).to_be_visible()

    #     expect(self.email).to_have_attribute("type", "email")

    #     self.email.fill(email)

    #     expect(self.email).to_have_value(email)
 
    # def fill_first_name(self, first_name: str):

    #     expect(self.first_name).to_be_visible()

    #     expect(self.first_name).to_have_attribute(

    #         "placeholder",

    #         "First Name"

    #     )

    #     self.first_name.fill(first_name)

    #     expect(self.first_name).to_have_value(first_name)
 
    # def fill_last_name(self, last_name: str):

    #     expect(self.last_name).to_be_visible()

    #     expect(self.last_name).to_have_attribute(

    #         "placeholder",

    #         "Last Name"

    #     )

    #     self.last_name.fill(last_name)

    #     expect(self.last_name).to_have_value(last_name)
 
    # def fill_password(self, password: str):

    #     expect(self.password).to_be_visible()

    #     expect(self.password).to_have_attribute("type", "password")

    #     self.password.fill(password)
 
    # def fill_repeat_password(self, password: str):

    #     expect(self.repeat_password).to_be_visible()

    #     expect(self.repeat_password).to_have_attribute("type", "password")

    #     self.repeat_password.fill(password)
 
    
    # def register(

    #     self,

    #     email: str,

    #     first_name: str,

    #     last_name: str,

    #     password: str,

    # ):

    #     expect(self.email).to_be_visible()

    #     self.email.fill(email)
 
    #     expect(self.first_name).to_be_visible()

    #     self.first_name.fill(first_name)
 
    #     expect(self.last_name).to_be_visible()

    #     self.last_name.fill(last_name)
 
    #     expect(self.password).to_be_visible()

    #     self.password.fill(password)
 
    #     expect(self.repeat_password).to_be_visible()

    #     self.repeat_password.fill(password)
 
    #     expect(self.continue_btn).to_be_enabled()

    #     self.continue_btn.click()
 