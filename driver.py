from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import constants as const


def get_driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    return driver
