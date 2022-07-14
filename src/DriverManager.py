from abc import ABC
from dataclasses import dataclass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@dataclass
class DriverManager(ABC):
    update = ChromeDriverManager()
    driver = webdriver.Chrome(executable_path=update.install())
