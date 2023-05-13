from Pages.exercisePage import ExercisePage
from Config.variables import Variables
from Utilities.logger import Logger
from Utilities.dataSetHandler import DataSetHandler
import io, pytest, json

with open("C:\\Test Automation\\Config\\dataset.json","r") as jsonFile:
      file = json.load(jsonFile)

tuple_list = DataSetHandler.dataSetHandler(file)
print(tuple_list)

class TestExercisePage():
    #-----   TESTS   -----
    @pytest.mark.parametrize("testName, newButtonName", tuple_list)
    def test_textInputExercise(self, testName, newButtonName, init_driver):
        logger = Logger.initLogger(testName, io.StringIO())
        exercisePage = ExercisePage(init_driver)
        flag = exercisePage.do_exercise(newButtonName, testName, logger)
        assert flag