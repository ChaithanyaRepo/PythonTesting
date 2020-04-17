from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver")
driver.get("https://www.flipkart.com/")

sleep(2)
# wait = WebDriverWait(driver, 5)
# wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "_2AkmmA _29YdH8")))
driver.find_element_by_class_name("_2AkmmA _29YdH8").click()

