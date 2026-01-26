import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:   # вложенная фикстура playwright из плагина pytest-playwright
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()
