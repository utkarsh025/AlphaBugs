from pages.base_page import BasePage

class FavouritesPage(BasePage):
    """Page Object for Favourites."""

    FAVOURITES_NAV_LINK = "#favourites"
    FAV_ITEMS = ".shelf-item"

    def open(self, base_url: str):
        self.navigate(f"{base_url}/favourites")
        self.wait_for_timeout(1000)

    def get_favourites_count(self) -> int:
        return self.page.locator(self.FAV_ITEMS).count()
