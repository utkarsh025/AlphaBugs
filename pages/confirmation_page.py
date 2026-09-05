from pages.base_page import BasePage

class ConfirmationPage(BasePage):
    """Page Object for Order Confirmation."""

    SUCCESS_MESSAGE = "text=Your Order has been successfully placed."
    ORDER_NUMBER_LABEL = "text=Your order number is"
    CONTINUE_SHOPPING_BTN = "button:has-text('CONTINUE SHOPPING')"
    DOWNLOAD_RECEIPT_BTN = "#downloadpdf"

    def is_order_confirmed(self) -> bool:
        return self.is_visible(self.SUCCESS_MESSAGE)

    def get_order_details_text(self) -> str:
        return self.page.inner_text("body")

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN, "Click Continue Shopping button")
        self.wait_for_timeout(1000)
