from playwright.sync_api import sync_playwright, Request, Response


# Логирование запросов
def log_request(request: Request):
    print(f"Request: {request.url}")


# Логирование ответов
def log_response(response: Response):
    print(f"Response: {response.url}, {response.status}")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    page.on("request", log_request)
    page.remove_listener("request", log_request)
    page.on("response", log_response)
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")