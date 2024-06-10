# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Configura tu driver aquí, por ejemplo, Chrome
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Opcional: ejecuta Chrome en modo headless
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()