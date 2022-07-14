from data import data
from selenium.webdriver.common.by import By
from DriverFunctionality import DriverFunctionality
from dataclasses import dataclass
from config.config_reader import Config


config = Config()


@dataclass
class App(DriverFunctionality):

    def setup(self) -> None:
        self.driver.get(config.read_file('data', 'link'))
        self.driver.implicitly_wait(2)

    def login(self) -> None:
        self.driver.find_element(By.ID, data.username).send_keys(config.read_file('data', 'username'))
        self.driver.find_element(By.ID, data.password).send_keys(config.read_file('data', 'password'))
        self.driver.find_element(By.NAME, data.button).click()

    def navigate(self) -> None:
        self.driver.find_element(By.ID, data.drop_down).click()
        self.driver.find_element(By.XPATH, data.log_work).click()
        self.driver.find_element(By.ID, data.time_spent).send_keys(config.read_file('data', 'work_hours'))

    def set_day(self) -> None:
        self.wait_for(By.XPATH, data.date, seconds=3)
        self.driver.find_element(By.XPATH, data.date).click()
        self._submit()

    def _submit(self) -> None:
        self.wait_for(By.ID, data.log, seconds=3)
        self.driver.find_element(By.ID, data.log).click()
        self.driver.find_element(By.ID, data.log).click()


def main() -> None:
    app = App()
    app.setup()
    app.login()
    app.navigate()
    app.set_day()
    app.exit()


if __name__ == '__main__':
    main()
