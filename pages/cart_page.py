from pages.base_page import BasePage

class CartPage(BasePage):
    """Page Object for Cart Drawer and cart operations."""

    CART_DRAWER = ".float-cart"
    CART_OPEN = ".float-cart--open"
    CART_BADGE = ".bag__quantity"
    CLOSE_BTN = ".float-cart__close-btn"
    CHECKOUT_BTN = ".buy-btn"
    SUBTOTAL_VAL = ".sub-price__val"
    CART_ITEMS = ".float-cart .shelf-item"
    DELETE_ITEM_BTN = ".shelf-item__del"

    def is_cart_open(self) -> bool:
        return self.is_visible(self.CART_OPEN)

    def get_badge_count(self) -> int:
        if self.is_visible(self.CART_BADGE):
            text = self.get_text(self.CART_BADGE)
            return int(text) if text.isdigit() else 0
        return 0

    def get_subtotal(self) -> str:
        if self.is_visible(self.SUBTOTAL_VAL):
            return self.get_text(self.SUBTOTAL_VAL)
        return "$ 0.00"

    def close_cart(self):
        if self.is_cart_open():
            self.click(self.CLOSE_BTN, "Close cart drawer")
            self.wait_for_timeout(300)

    def proceed_to_checkout(self):
        self.logger.info("Proceeding to checkout from cart")
        self.click(self.CHECKOUT_BTN, "Click Checkout button in cart")
        self.wait_for_timeout(1000)

    def get_cart_items_count(self) -> int:
        return self.page.locator(self.CART_ITEMS).count()

    def remove_first_item(self):
        if self.is_visible(self.DELETE_ITEM_BTN):
            self.click(self.DELETE_ITEM_BTN, "Remove item from cart")
            self.wait_for_timeout(500)
