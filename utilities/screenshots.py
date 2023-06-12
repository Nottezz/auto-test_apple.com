import allure
import datetime


def get_screenshot():
    now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
    name_screenshot = 'screenshot_' + now_date
    allure.attach.file('/home/nikita/PycharmProjects/apple.com/screenshots/', name_screenshot,
                       attachment_type=allure.attachment_type.PNG)
