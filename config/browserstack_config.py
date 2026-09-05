import os
import json
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

class BrowserStackConfig:
    """BrowserStack Automate capabilities and connection configuration."""
    USERNAME = os.getenv("BROWSERSTACK_USERNAME", "")
    ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY", "")
    PROJECT_NAME = os.getenv("BSTACK_PROJECT_NAME", "AlphaBugs")
    BUILD_NAME = os.getenv("BSTACK_BUILD_NAME", "AlphaBugs Testathon E2E Suite")
    
    PLATFORMS = {
        "chrome_win11": {
            "browser": "chrome",
            "browser_version": "latest",
            "os": "windows",
            "os_version": "11"
        },
        "edge_win10": {
            "browser": "edge",
            "browser_version": "latest",
            "os": "windows",
            "os_version": "10"
        },
        "safari_sonoma": {
            "browser": "playwright-webkit",
            "os": "osx",
            "os_version": "sonoma"
        },
        "firefox_win11": {
            "browser": "playwright-firefox",
            "os": "windows",
            "os_version": "11"
        }
    }

    @classmethod
    def get_capabilities(cls, platform_key="chrome_win11", test_name="E2E Test"):
        """Constructs capabilities dictionary for a test run."""
        base_caps = cls.PLATFORMS.get(platform_key, cls.PLATFORMS["chrome_win11"]).copy()
        base_caps.update({
            "browserstack.username": cls.USERNAME,
            "browserstack.accessKey": cls.ACCESS_KEY,
            "project": cls.PROJECT_NAME,
            "build": cls.BUILD_NAME,
            "name": test_name,
            "browserstack.networkLogs": "true",
            "browserstack.console": "info",
            "browserstack.debug": "true"
        })
        return base_caps

    @classmethod
    def get_cdp_url(cls, platform_key="chrome_win11", test_name="E2E Test"):
        """Returns the WebSocket CDP endpoint for Playwright remote execution."""
        caps = cls.get_capabilities(platform_key, test_name)
        encoded_caps = urllib.parse.quote(json.dumps(caps))
        return f"wss://cdp.browserstack.com/playwright?caps={encoded_caps}"
