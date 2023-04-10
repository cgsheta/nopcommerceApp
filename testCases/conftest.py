import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser.........")
    else:
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

##################### Pytest HTML Report###########
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Chirag'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)