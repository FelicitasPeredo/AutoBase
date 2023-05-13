import pytest
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Config.variables import Variables

# set up and tear down of the new selenium web driver session invoked per test
@pytest.fixture()
def init_driver():
    #SET UP
    # selenium web driver remote session to run tests with selenium grid hub
    if Variables.executionAgent == "chromeRemote":
        chrome_options = Options()
        chrome_options.add_argument('start-maximized')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument("--disable-infobars")
        web_driver = webdriver.Remote(command_executor=Variables.hub, options=chrome_options)
    # selenium web driver local session to run tests in local machine
    elif Variables.executionAgent == "chromeLocal":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument("--disable-infobars")
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    # request.cls.driver = web_driver
    yield web_driver
    #TEAR DOWN
    web_driver.quit()


