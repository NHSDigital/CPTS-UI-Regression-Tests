from playwright.sync_api import Page, expect


class MainPage:
    MAIN_HEADING: str = "app-main-heading"
    SUB_HEADING: str = "app-sub-heading"

    def __init__(self, page: Page):
        self.page = page

    def verify_headers_text(self):
        expect(self.page.get_by_text("NHS website for England")).to_be_visible()
        expect(
            self.page.get_by_text(
                "Find information and services to help you manage your health"
            )
        ).to_be_visible()
