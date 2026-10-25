# Author:Yi Sun(Tim) 2022-08-05

"""Browser creation. The only place that knows how a Selenium driver is built
(Selenium >= 4.6 resolves drivers itself via Selenium Manager)."""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def create_driver(browser: str = "firefox", headless: bool = False):
    browser = browser.lower()
    if browser == "firefox":
        opts = FirefoxOptions()
        if headless:
            opts.add_argument("-headless")
        driver = webdriver.Firefox(options=opts)
    elif browser == "chrome":
        opts = ChromeOptions()
        if headless:
            opts.add_argument("--headless=new")
        driver = webdriver.Chrome(options=opts)
    elif browser == "edge":
        opts = EdgeOptions()
        if headless:
            opts.add_argument("--headless=new")
        driver = webdriver.Edge(options=opts)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    if headless:
        driver.set_window_size(1920, 1080)
    else:
        driver.maximize_window()
    return driver   # no implicit wait: explicit waits only (never mix the two)
