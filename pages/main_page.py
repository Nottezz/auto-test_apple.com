import allure
from  base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):
    url = "https://www.apple.com/ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods
    def open_page(self):
        Logger.add_start_step(method='open_page')
        self.driver.get(self.url)
        self.driver.maximize_window()
        Logger.add_end_step(url=self.driver.current_url, method='open_page')
