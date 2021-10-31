from webdriver_manager import driver


class ScreenShots(object):

    def __init__(self):
        self.driver = driver

    def screenshot(self, path):
        directory = "C:\\Users\\Arumugam\\PycharmProjects\\ECommerce_Demo\\Screenshots"
        self.driver.get_screenshot_as_file(directory + path)
