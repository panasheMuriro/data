import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Attempt to load the page with extended timeout and `networkidle` wait condition
    page.goto(
        "https://www.imdb.com/title/tt5071412/reviews/?ref_=ttrt_sa_3&spoilers=EXCLUDE",
        timeout=60000,  # Extend timeout to 60 seconds
        wait_until="networkidle"
    )
    
    # Interact with the page
    page.get_by_test_id("tturv-pagination").get_by_role("button", name="All").click()

    # Close the context and browser
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
