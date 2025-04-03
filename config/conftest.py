import logging
import os
import time
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

URL = os.getenv('URL')
BROWSER = os.getenv('BROWSER', 'chromium')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
_logger = logging.getLogger(__name__)


@pytest.fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(params=["chromium"])
def base_page(request, get_playwright):
    browser_type = request.param
    if browser_type == "chromium":
        browser = get_playwright.chromium
    elif browser_type == "firefox":
        browser = get_playwright.firefox
    else:
        raise ValueError(f"Unsupported browser type: {browser_type}")

    _logger.info('Launching the browser and opening a new page')
    browser_instance = browser.launch(headless=True)
    page = browser_instance.new_page()
    page.goto(URL)
    yield page
    _logger.info('Closing the browser after the test')
    page.close()
    browser_instance.close()


def pytest_sessionfinish(session) -> None:
    duration = session.duration
    reporter = session.config.pluginmanager.get_plugin('terminalreporter')
    reporter.write_sep('=', f'duration: {duration} seconds', yellow=True, bold=True)


@pytest.fixture(autouse=True)
def log_test_execution_time(request):
    start_time = time.time()
    yield
    end_time = time.time()
    execution_time = end_time - start_time
    test_name = request.node.name
    _logger.info(f"Test '{test_name}' executed in {execution_time:.2f} seconds.")


@pytest.fixture(scope='function', autouse=True)
def failed_check(request) -> None:
    yield
    if request.node.rep_setup.failed:
        logging.error(f'Setting up test failed! {request.node.nodeid}')
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            logging.error(f'Executing test failed! {request.node.nodeid}')
