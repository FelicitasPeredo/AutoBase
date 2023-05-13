from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 45, poll_frequency=0.1)
        self.wait15 = WebDriverWait(self.driver, 15)
        self.wait10 = WebDriverWait(self.driver, 10)
        self.wait5 = WebDriverWait(self.driver, 5)
        self.actions = ActionChains(self.driver)

    #-----FINDS----#

    # returns a unique web element
    def findElement(self, locator):
        return self.driver.find_element(By.XPATH,locator)

    # returns a list of web elements
    def findElements(self, locator):
        return self.driver.find_elements(By.XPATH,locator)
    
    # check if element it visible to user or not, returns True or False
    def isDisplayed(self, locator):
        return self.findElement(locator).is_displayed()

    #-----CLICKS----#

    # selenium web driver click
    # waits an element to be visible and clickeable and then clicks it
    def click(self, locator):
        self.waitUntilElementIsClickeable(locator)
        self.findElement(locator).click()

    # waits an element to be visible and enabled such that you can click it
    def waitUntilElementIsClickeable(self, locator):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
    
    # JS click
    # waits an element to be visible and clickeable and then clicks it
    def JSClick(self, locator):
        self.waitUntilElementIsClickeable(locator)
        self.driver.execute_script("arguments[0].click();", self.findElement(locator))

    #-----INPUTS----#

    # input content in editable text fields
    def sendKeys(self, locator, textValue):
        self.findElement(locator).send_keys(textValue)

    # uploads a file
    def uploadFile(self, locator, root):
        self.sendKeys(locator, root)

    # input content in editable text fields with ActionChains
    def actionsSendKeys(self, value):
            self.actions.send_keys(value)
            self.actions.perform()

    # clears a text input value
    def clearTextField(self, locator):
        self.findElement(locator).clear()

    #-----GETS----#

    # returns the page's title
    def getTitle(self):
        return self.driver.title
    
    # returns an element's text
    def getText(self, locator):
        return self.findElement(locator).text
    
    # returns the value of a specified atribute of an element
    def getAttribute(self, locator, attribute):
        self.waitUntilVisible(locator)
        return self.findElement(locator).get_attribute(attribute)
    
    # returns the text content of an element
    def getTextContentOfElement(self, locator):
        label = self.findElement(locator)
        return label.get_attribute("textContent")

    # returns the text content of an element
    def getStyle(self, locator):
        style = self.findElement(locator)
        return style.get_attribute("style")

    # returns a list of element's text content
    def getTextContentOfElements(self, locator):
        listElements = self.findElements(locator)
        listResultsText = list(map(lambda e: e.get_attribute("textContent"), listElements))
        return listResultsText

    #-----SCROLLS----#

    # waits element to be present on the DOM and scrolls to element
    def scrollIntoViewAnElement(self, locator):
        self.waitUntilLocatedInDOM(locator)
        self.scrollIntoView(locator)

    # scrolls into view a web element
    def scrollIntoView(self, locator):
        element = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

    # select a dropdown value: clicks the dropdown and then clicks the option
    def selectDropdownValue(self, locator, locatorOption):
        self.scrollIntoViewAnElement(locator)
        self.waitUntilElementIsClickeable(locator)
        self.click(locator)
        self.waitUntilElementIsClickeable(locatorOption)
        self.click(locatorOption)

    #-----SWITCHS----#
    
    # a list of iframes is captured, then the driver switches to the iframe in the position specified
    def switchFrame(self, locator, frameIndex):
        iframes = self.findElements(locator)
        self.driver.switch_to.frame(iframes[(frameIndex)])

    # switchs the driver focus to the window specified
    def switchToTab(self, tabIndex):
        self.driver.switch_to.window(self.driver.window_handles[tabIndex]) # index starts from 0

    #-----WAITS----#

    # waits 45s an element to be present on the DOM of a page and visible
    def waitUntilVisible(self, locator):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    # waits 15s an element to be present on the DOM of a page and visible
    def waitUntilVisible15(self, locator):
        self.wait15.until(EC.visibility_of_element_located((By.XPATH, locator)))

    # waits 10s an element to be present on the DOM of a page and visible
    def waitUntilVisible5(self, locator):
        self.wait10.until(EC.visibility_of_element_located((By.XPATH, locator)))

    # waits 5s an element to be present on the DOM of a page and visible
    def waitUntilVisible5(self, locator):
        self.wait5.until(EC.visibility_of_element_located((By.XPATH, locator)))

    # waits 45s an element to be present on the DOM of a page
    def waitUntilLocatedInDOM(self, locator):
        self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))

    # waits until an element is either invisible or not present on the DOM
    def waitUntilNotVisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, locator)))

    # waits 45s number of windows to be the one specified
    def waitUntilNumberOfWindowsToBe(self, number):
        self.wait.until(EC.number_of_windows_to_be(number))

    # waits 15s number of windows to be the one specified
    def wait15UntilNumberOfWindowsToBe(self, number):
        self.wait15.until(EC.number_of_windows_to_be(number))

    # waits if the given text is present in the element’s attribute
    def waitUntilAtributeHasText(self, locator, attribute, value):
        self.wait.until(EC.text_to_be_present_in_element_attribute((By.XPATH, locator), attribute, value))

    # waits until the current url contains a case-sensitive substring
    def waitUntilUrlContains(self, text):
        self.wait.until(EC.url_contains(text))

    #-----SCREENSHOTS----#

    def saveScreenshot(self, image_name):
        self.driver.save_screenshot(f'C:\\CSE Test Automation\\Screenshots\\{image_name}.png')

    def saveElementScreenshot(self, locator, image_name):
        element = self.findElement(locator)
        element.screenshot(f'C:\\CSE Test Automation\\Screenshots\\{image_name}.png')
