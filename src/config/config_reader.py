from dataclasses import dataclass
from configparser import ConfigParser
global Config


@dataclass
class Config:

    path: str = 'C:\\Users\\evgenyp\\AppData\\JiraLogWorkAutomation\\src\\config\\config.ini'

    def read_file(self, key: str, value: str):
        config_parser = ConfigParser()
        config_parser.read(self.path)

        return config_parser.get(key, value)
