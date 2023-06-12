import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger



class Mac_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    mac_button = '//a[@class="ac-gn-link ac-gn-link-mac"]'
    learn_more = '//a[@data-analytics-title="learn more about macbook pro"]'
    # Locators Why mac
    why_mac = '//a[@data-analytics-title="why mac"]'
    settings_button = '//*[@id="main"]/article[1]/section[1]/div/div/button'
    work_button = '//*[@id="main"]/article[1]/section[2]/div/div/button'
    close_button = '//button[@aria-label="Close"]'
    # Locators Tech Specs
    tech_specs = '//a[@data-analytics-title="tech specs"]'
    button_16 = '//*[@id="table-16-label"]'
    button_14 = '//*[@id="table-14-label"]'
    macos_more = '//a[@data-analytics-title="learn more - macos"]'
    macos_monterey = '//*[@id="ac-localnav"]/div/div[2]/div[1]/a'

    # Getters

    def get_mac_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mac_button)))

    def get_learn_more(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.learn_more)))

    def get_why_mac(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.why_mac)))

    def get_settings_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.settings_button)))

    def get_work_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.work_button)))

    def get_close_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_button)))

    def get_tech_specs(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tech_specs)))

    def get_button_16(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_16)))

    def get_button_14(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_14)))

    def get_macos_more(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.macos_more)))

    def get_macos_monterey(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.macos_monterey)))


    # Actions

    def click_mac_button(self):
        self.get_mac_button().click()
        print('Open Mac page')

    def click_learn_more(self):
        self.get_learn_more().click()
        print('Open Macbook Pro page')

    def click_why_mac(self):
        self.get_why_mac().click()
        print('Open page "Why mac?"')

    def click_settings_button(self):
        self.get_settings_button().click()
        print('Learn more about setting up"')

    def click_work_button(self):
        self.get_work_button().click()
        print('Learn more about job opportunities"')

    def click_close_button(self):
        self.get_close_button().click()
        print('Clicking on closing details"')

    def click_tech_specs(self):
        self.get_tech_specs().click()
        print('Open tech specs Macbook Pro')

    def click_button_16(self):
        self.get_button_16().click()
        print('Click to 16` button')

    def click_button_14(self):
        self.get_button_14().click()
        print('Return to 14`')

    def click_macos_more(self):
        self.get_macos_more().click()
        print('Open detail info about MacOS')

    # Methods

    def macbook_pro(self):
        Logger.add_start_step(method='macbook_pro')
        self.click_mac_button()
        self.click_learn_more()
        self.assert_word(self.driver.current_url, 'https://www.apple.com/ru/macbook-pro-14-and-16/')
        self.driver.execute_script('window.scrollTo(0, 1500)')
        self.click_why_mac()
        self.assert_word(self.driver.current_url, 'https://www.apple.com/ru/macbook-pro-14-and-16/why-mac/')
        self.driver.execute_script('window.scrollTo(0, 500)')
        self.click_settings_button()
        self.click_close_button()
        self.driver.execute_script('window.scrollTo(0, 500)')
        self.click_work_button()
        self.click_close_button()
        self.click_tech_specs()
        self.assert_word(self.driver.current_url, 'https://www.apple.com/ru/macbook-pro-14-and-16/specs/')
        self.click_button_16()
        self.click_button_14()
        self.driver.execute_script('window.scrollTo(0, 1500)')
        self.click_macos_more()
        self.assert_word(self.get_macos_monterey().text, 'macOS Monterey')
        self.assert_word(self.driver.current_url, 'https://www.apple.com/ru/macos/monterey/')
        Logger.add_end_step(url=self.driver.current_url, method='macbook_pro')
