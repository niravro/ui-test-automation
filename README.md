# pytest + selenium starter
# pytest + selenium starter

This small starter shows how to write a headless Selenium UI test using pytest.

Files:
- `requirements.txt` - Python dependencies
- `tests/conftest.py` - pytest fixtures to provide a Selenium WebDriver (headless Chrome)
- `tests/test_google.py` - a simple test that opens example.com and asserts the title

Setup (macOS, zsh):

1. Create a virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run tests:

```bash
pytest -q
```

Notes:
- This uses `webdriver-manager` to download a matching ChromeDriver automatically.
- If you prefer Firefox, swap to `geckodriver` and `selenium.webdriver.Firefox`.

CI tips
-------
- On GitHub Actions use `actions/checkout` + `actions/setup-python` and install Chrome (or use a runner that already has it). Then `pip install -r requirements.txt` and run `pytest`.
- Cache pip dependencies to speed up runs.

Troubleshooting
---------------
- If ChromeDriver fails to start, ensure a matching Chrome version is installed or allow `webdriver-manager` network access so it can download the driver.
- For flaky tests, prefer Selenium's `WebDriverWait` with expected conditions over fixed `time.sleep()`.

Next steps
----------
- Add page object classes under `tests/pages/` to encapsulate UI interactions.
- Add tests for login flows with parametrized inputs.
- Integrate reporting with `pytest-html` or similar plugins.

Enjoy exploring UI automation with pytest + Selenium!
