import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    def assert_word(self, word, result):
        assert word == result
        print('Name is good')