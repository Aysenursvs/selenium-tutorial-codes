import os
from . import constants as const
from selenium import webdriver

current_dir = os.path.dirname(os.path.abspath(__file__))
chromedriver_path = os.path.join(current_dir, "..", "..", "chromedriver")

class Booking(webdriver.Chrome):
    def __init__(self, executable_path=chromedriver_path, teardown=False):
       self.driver_path = executable_path
       self.teardown = teardown
       os.environ["PATH"] += os.pathsep + self.driver_path
       super(Booking, self).__init__()
       self.implicitly_wait(15)
       self.maximize_window()

    def __enter__(self):
        return self     

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        



