from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object for Authentication / Sign-In flow."""

    USERNAME_DROPDOWN = "#username"
    PASSWORD_DROPDOWN = "#password"
    LOGIN_BUTTON = "#login-btn"
    ERROR_MESSAGE = ".api-error"
    USER_HEADER = "span.username"
    LOGOUT_BTN = "#logout"

    def open(self, base_url: str):
        self.navigate(f"{base_url}/signin")
        self.page.wait_for_selector(self.USERNAME_DROPDOWN)

    def select_username(self, username: str):
        self.logger.info(f"Selecting username: {username}")
        self.click(self.USERNAME_DROPDOWN, f"Click Username dropdown")
        self.page.keyboard.type(username)
        self.page.keyboard.press("Enter")
        self.wait_for_timeout(300)

    def select_password(self, password: str):
        self.logger.info("Selecting password")
        self.click(self.PASSWORD_DROPDOWN, f"Click Password dropdown")
        self.page.keyboard.type(password)
        self.page.keyboard.press("Enter")
        self.wait_for_timeout(300)

    def click_login(self):
        self.click(self.LOGIN_BUTTON, "Click Log In button")

    def login(self, username: str, password: str):
        self.select_username(username)
        self.select_password(password)
        self.click_login()
        self.wait_for_timeout(1000)

    def get_error_message(self) -> str:
        if self.is_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""

    def get_logged_in_user(self) -> str:
        if self.is_visible(self.USER_HEADER):
            return self.get_text(self.USER_HEADER)
        return ""

    def logout(self):
        if self.is_visible(self.LOGOUT_BTN):
            self.click(self.LOGOUT_BTN, "Click Logout")
            self.wait_for_timeout(500)
