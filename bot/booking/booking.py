import os
from .constants import BASE_URL
from selenium import webdriver

current_dir = os.path.dirname(os.path.abspath(__file__))
chromedriver_path = os.path.join(current_dir, "..", "..", "chromedriver")

class Booking(webdriver.Chrome):
    def __init__(self, executable_path=chromedriver_path):
       self.driver_path = executable_path
       os.environ["PATH"] += os.pathsep + self.driver_path
       super(Booking, self).__init__()

    def land_first_page(self):
        self.get(BASE_URL)
        



