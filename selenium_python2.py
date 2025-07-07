import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

current_dir = os.path.dirname(os.path.abspath(__file__))
chromedriver_path = os.path.join(current_dir, "chromedriver")

service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(10)  # Set an implicit wait time

driver.get("http://localhost/")  # Replace with your local server URL

text_input = driver.find_element(By.NAME, "username")  # Adjust the selector as needed
text_input.send_keys(Keys.NUMPAD1)

text_input2 = driver.find_element(By.NAME, "password")  # Adjust the selector as needed
text_input2.send_keys(Keys.NUMPAD9)

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")  # Adjust the selector as needed
login_button.click()



time.sleep(5)




