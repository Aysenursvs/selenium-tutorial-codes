import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
chromedriver_path = os.path.join(current_dir, "chromedriver")

service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

driver.implicitly_wait(10)

add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
add_button.click()
#time.sleep(5)  # Wait for the element to be added
delete_button = driver.find_element(By.CLASS_NAME, "added-manually")
delete_button.click()
#time.sleep(5)  # Wait for the element to be added

#WebDriverWait(driver,10).until(
#    EC.presence_of_element_located((By.XPATH, "//div[@id='elements']/button[@class='added-manually']"))
#)