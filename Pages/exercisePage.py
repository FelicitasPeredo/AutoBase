from Pages.basePage import BasePage
from Config.locators import Locators
from Config.variables import Variables


class ExercisePage(BasePage):
    
    #----  INITIALIZER  ----
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Variables.base_url_input)

    #----  METHODS  ----
    def get_page_title(self, logger):
        self.saveScreenshot('exercise_page_title')
        return self.getTitle()

    def do_exercise(self, value, testName, logger):
        self.sendKeys(Locators.text_input, value)
        self.saveElementScreenshot(Locators.text_input, 'text_input_'+testName)
        logger.info(f'New button name populated correctly with the following value: {value} ')
        self.click(Locators.updating_button)
        self.saveElementScreenshot(Locators.updating_button, 'updating_button_'+testName)
        logger.info(f'Updating button name btn clicked successfully')
        return self.getText(Locators.updating_button)