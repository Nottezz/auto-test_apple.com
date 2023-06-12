import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from pages.main_page import Main_page
from pages.mac_page import Mac_page


def test_mac():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://www.apple.com/ru/')

    print('Start test')

    mp = Main_page(driver)
    mp.open_page()

    mcp = Mac_page(driver)
    mcp.macbook_pro()

    print('Finish test')
