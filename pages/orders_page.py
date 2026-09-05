from pages.base_page import BasePage

class OrdersPage(BasePage):
    """Page Object for Orders History."""

    ORDERS_NAV_LINK = "#orders"
    ORDER_CARD = ".order"

    def open(self, base_url: str):
        self.navigate(f"{base_url}/orders")
        self.wait_for_timeout(1000)

    def get_orders_count(self) -> int:
        return self.page.locator(self.ORDER_CARD).count()

    def get_page_text(self) -> str:
        return self.page.inner_text("body")
