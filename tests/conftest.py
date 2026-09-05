import pytest
from playwright.sync_api import sync_playwright
from config.browserstack_config import BrowserStackConfig
from config.environments import EnvironmentConfig
from utils.bstack_helper import BrowserStackHelper

@pytest.fixture(scope="function")
def page(request):
    """Playwright page fixture supporting both BrowserStack Cloud and local execution."""
    test_name = request.node.name
    run_on_bstack = EnvironmentConfig.RUN_ON_BSTACK
    
    with sync_playwright() as playwright:
        if run_on_bstack and BrowserStackConfig.USERNAME and BrowserStackConfig.ACCESS_KEY:
            cdp_url = BrowserStackConfig.get_cdp_url(test_name=test_name)
            browser = playwright.chromium.connect(cdp_url)
            context = browser.new_context()
            pg = context.new_page()
            BrowserStackHelper.annotate(pg, f"Starting test: {test_name}")
            
            yield pg
            
            # Determine test outcome for BrowserStack session status
            rep = getattr(request.node, "rep_call", None)
            if rep and rep.failed:
                BrowserStackHelper.set_session_status(pg, "failed", str(rep.longrepr))
            else:
                BrowserStackHelper.set_session_status(pg, "passed", f"Test {test_name} passed successfully")
            
            browser.close()
        else:
            browser = playwright.chromium.launch(headless=True)
            context = browser.new_context()
            pg = context.new_page()
            
            yield pg
            browser.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
