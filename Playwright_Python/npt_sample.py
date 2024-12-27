import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:

    page.goto("/")
    page.get_by_role("heading", name="ID[me] Sign-In Page").click()
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("username")
    page.get_by_role("button", name="Next").click()
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").dblclick()
    page.get_by_role("textbox", name="Password").fill("password")
    page.get_by_role("button", name="Verify").click()
    page.get_by_role("button", name="Verify").click()
    page.goto("/")
    page.get_by_label("NORTH AMERICA-ADMIN").check()
    page.get_by_role("button", name="Ok").click()
    page.get_by_role("button", name="Real-Time Price Lookup").click()
    page.locator("div").filter(has_text=re.compile(r"^Loading\.\.\.$")).nth(1).click()
    page.get_by_label("Site Cluster Set").check()
    page.get_by_label("Product Filter").check()
    page.locator("#siteClusterSet-wrapper svg").click()
    page.get_by_role("option", name="Nike Factory Stores").click()
    page.get_by_test_id("autocomplete").get_by_label("Product Filter").click()
    page.get_by_test_id("autocomplete").get_by_label("Product Filter").fill("per")
    page.get_by_role("option", name="Performance variants").click()
    page.get_by_role("button", name="Execute").click()
    page.get_by_text("-419-NIKE-01").nth(3).click()