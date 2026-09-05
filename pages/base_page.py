from playwright.sync_api import Page, Locator
from utils.logger import get_logger
from utils.bstack_helper import BrowserStackHelper

class BasePage:
    """Base class for all Page Objects providing encapsulated interactions and BrowserStack telemetry."""
    
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def navigate(self, url: str):
        self.logger.info(f"Navigating to {url}")
        BrowserStackHelper.annotate(self.page, f"Navigate to: {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    def wait_for(self, selector: str, timeout: int = 10000) -> Locator:
        return self.page.locator(selector).first

    def click(self, selector: str, step_desc: str = ""):
        if step_desc:
            self.logger.info(step_desc)
            BrowserStackHelper.annotate(self.page, step_desc)
        self.page.locator(selector).first.click()

    def fill(self, selector: str, text: str, step_desc: str = ""):
        if step_desc:
            self.logger.info(step_desc)
            BrowserStackHelper.annotate(self.page, step_desc)
        locator = self.page.locator(selector).first
        locator.fill(text)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).first.inner_text().strip()

    def is_visible(self, selector: str, timeout: int = 5000) -> bool:
        try:
            return self.page.locator(selector).first.is_visible(timeout=timeout)
        except Exception:
            return False

    def get_current_url(self) -> str:
        return self.page.url

    def wait_for_timeout(self, ms: int):
        self.page.wait_for_timeout(ms)
