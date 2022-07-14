from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from DriverManager import DriverManager


class DriverFunctionality(DriverManager):

    def wait_for(self, by: By, element: str, seconds=0):
        wait = WebDriverWait(self.driver, seconds)

        try:
            wait.until(EC.visibility_of_element_located((by, element)))

        except NoSuchElementException as e:
            e.message = 'no such element'
            print(e.message)

    def exit(self):
        self.driver.close()
        self.driver.quit()
