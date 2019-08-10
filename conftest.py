import re
import pytest


@pytest.fixture()
def chrome_options(request, chrome_options):
    # Disable the W3C when initializing the Chrome driver
    chrome_options.add_experimental_option("w3c", False)
    chrome_options.add_argument("--start-maximized")

    # Workaround, depending on test function name with or without "mobile" in it Chrome will run with different options
    # don't know how to use different chrome_options fixture for different tests
    for key in dict(request.keywords):
        if re.search("mobile", key):
            device_name = {"deviceName": "iPhone X"}
            chrome_options.add_experimental_option("mobileEmulation", device_name)
            # device_metrics = {"deviceMetrics": {"width": 760}}
            # chrome_options.add_experimental_option("mobileEmulation", device_metrics)
    return chrome_options


@pytest.fixture
def connect_to_url(driver):
    driver.get("http://blog.csssr.ru/qa-engineer/")
    return connect_to_url


