from selenium import webdriver
from time import sleep

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path='/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver',options=chromeOptions)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)