from typing import List
from pages.base_page import BasePage

class ProductPage(BasePage):
    """Page Object for Product Catalog, Filtering, and Sorting."""

    PRODUCT_ITEM = ".shelf-item"
    PRODUCT_TITLE = ".shelf-item__title"
    PRODUCT_PRICE = ".shelf-item__price .val b"
    ADD_TO_CART_BTN = ".shelf-item__buy-btn"
    PRODUCTS_COUNT = ".products-found"
    SORT_DROPDOWN = "select"
    FAVORITE_BTN = "button.MuiIconButton-root"
    PRODUCT_IMAGE = ".shelf-item__thumb img"

    def open(self, base_url: str):
        self.navigate(base_url)
        self.page.wait_for_selector(self.PRODUCT_ITEM)

    def get_product_count(self) -> int:
        return self.page.locator(self.PRODUCT_ITEM).count()

    def get_all_product_titles(self) -> List[str]:
        return [el.inner_text().strip() for el in self.page.locator(self.PRODUCT_TITLE).all()]

    def filter_by_vendor(self, vendor_name: str):
        self.logger.info(f"Applying vendor filter: {vendor_name}")
        self.click(f"text={vendor_name}", f"Filter by vendor: {vendor_name}")
        self.wait_for_timeout(800)

    def sort_by(self, sort_value: str):
        self.logger.info(f"Sorting products by: {sort_value}")
        self.page.select_option(self.SORT_DROPDOWN, sort_value)
        self.wait_for_timeout(800)

    def add_product_to_cart(self, index: int = 0):
        self.logger.info(f"Adding product index {index} to cart")
        buttons = self.page.locator(self.ADD_TO_CART_BTN)
        buttons.nth(index).click()
        self.wait_for_timeout(500)

    def add_product_by_title(self, title: str):
        self.logger.info(f"Adding product '{title}' to cart")
        shelf_item = self.page.locator(f".shelf-item:has-text('{title}')")
        shelf_item.locator(self.ADD_TO_CART_BTN).click()
        self.wait_for_timeout(500)

    def get_prices(self) -> List[float]:
        """Extracts visible prices as floating point numbers for sorting validation."""
        prices = []
        for el in self.page.locator(self.PRODUCT_PRICE).all():
            text = el.inner_text().replace("$", "").strip()
            try:
                prices.append(float(text))
            except ValueError:
                pass
        return prices

    def check_broken_images(self) -> int:
        """Returns the number of product images with failed/broken sources."""
        broken = 0
        images = self.page.locator(self.PRODUCT_IMAGE).all()
        for img in images:
            src = img.get_attribute("src")
            if not src or "undefined" in src or "null" in src:
                broken += 1
        return broken
