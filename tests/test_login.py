from pages.login_page import LoginPage


def test_login_success(browser):
    page = LoginPage(browser)
    page.load()
    page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in page.flash.text
