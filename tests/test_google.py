def test_example_domain_title(browser):
    """Open example.com and assert the title is 'Example Domain' (stable target)."""
    browser.get("https://example.com")
    assert "Example Domain" in browser.title
