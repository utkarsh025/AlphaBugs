import json
import logging
import requests

logger = logging.getLogger(__name__)

class BrowserStackHelper:
    """Helper utilities for BrowserStack session management and step annotations."""
    
    @staticmethod
    def annotate(page, data: str, level: str = "info"):
        """Logs a custom step annotation that appears in the BrowserStack session video timeline."""
        try:
            payload = json.dumps({"action": "annotate", "arguments": {"data": data, "level": level}})
            page.evaluate("_ => {}", f"browserstack_executor: {payload}")
        except Exception as e:
            logger.debug(f"Annotation failed (harmless if running locally): {e}")

    @staticmethod
    def set_session_status(page, status: str, reason: str = ""):
        """Marks the session status as passed or failed in BrowserStack Automate."""
        try:
            payload = json.dumps({"action": "setSessionStatus", "arguments": {"status": status, "reason": reason}})
            page.evaluate("_ => {}", f"browserstack_executor: {payload}")
        except Exception as e:
            logger.debug(f"Set session status failed (harmless if running locally): {e}")

    @staticmethod
    def fetch_latest_build_info(username: str, access_key: str):
        """Fetches latest build metadata including public shareable link from BrowserStack Automate REST API."""
        try:
            url = "https://api.browserstack.com/automate/builds.json?limit=1"
            response = requests.get(url, auth=(username, access_key), timeout=10)
            if response.status_code == 200:
                builds = response.json()
                if builds:
                    build_data = builds[0].get("automation_build", {})
                    return {
                        "name": build_data.get("name"),
                        "hashed_id": build_data.get("hashed_id"),
                        "status": build_data.get("status"),
                        "public_url": build_data.get("public_url")
                    }
        except Exception as e:
            logger.error(f"Failed to fetch BrowserStack build info: {e}")
        return None
