import os
from . import constans as const
from selenium import webdriver

current_dir = os.path.dirname(os.path.abspath(__file__))
chromedriver_path = os.path.join(current_dir, "..", "..", "chromedriver")

class Booking(webdriver.Chrome):
    def __init__(self, executable_path=chromedriver_path):
       self.driver_path = executable_path
       super(Booking, self).__init__()

    def land_first_page(self):
        self.get(const.BASE_URL)
        self.implicitly_wait(10)


