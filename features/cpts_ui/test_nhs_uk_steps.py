from pytest_bdd import scenario, when, then

from pages.main_page import MainPage


@scenario("sample.feature", "user can navigate to the NHS UK page")
def test_user_can_navigate():
    print("starting bdd test")


@when("I go to the NHS UK website")
def goto_page(page):
    page.goto("https://nhs.uk")


@then("I am on the NHS UK website")
def verify_on_page(page):
    main_page = MainPage(page)
    main_page.verify_headers_text()
