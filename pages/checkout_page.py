from pages.base_page import BasePage

class CheckoutPage(BasePage):
    """Page Object for Shipping and Checkout."""

    FIRST_NAME_INPUT = "#firstNameInput"
    LAST_NAME_INPUT = "#lastNameInput"
    ADDRESS_INPUT = "#addressLine1Input"
    PROVINCE_INPUT = "#provinceInput"
    POST_CODE_INPUT = "#postCodeInput"
    SUBMIT_BTN = "#checkout-shipping-continue"

    def fill_shipping_details(self, first_name: str, last_name: str, address: str, province: str, post_code: str):
        self.logger.info("Filling checkout shipping details")
        self.fill(self.FIRST_NAME_INPUT, first_name, "Enter First Name")
        self.fill(self.LAST_NAME_INPUT, last_name, "Enter Last Name")
        self.fill(self.ADDRESS_INPUT, address, "Enter Address")
        self.fill(self.PROVINCE_INPUT, province, "Enter State/Province")
        self.fill(self.POST_CODE_INPUT, post_code, "Enter Postal Code")

    def submit_shipping(self):
        self.logger.info("Submitting shipping form")
        self.click(self.SUBMIT_BTN, "Click Continue Shipping / Submit")
        self.wait_for_timeout(1500)
