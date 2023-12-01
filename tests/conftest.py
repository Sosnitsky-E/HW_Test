import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def chrome_options():
    options = Options()
    # options.add_argument('--headless')
    options.page_load_strategy = 'none'
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return options


@pytest.fixture(scope="function")
def driver(chrome_options):
    """
    Browser creating fixture
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    print("\nopen browser")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    print("\nquit browser")
    driver.quit()
