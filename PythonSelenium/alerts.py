from selenium import webdriver
from time import sleep
# validateText = "Option3"

driver = webdriver.Chrome(executable_path="/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Positive case
driver.find_element_by_css_selector("input#name").send_keys("Option3")
validateText = driver.find_element_by_xpath("//input[@id='name']").text
driver.find_element_by_xpath("//input[@value='Alert']").click()
alert = driver.switch_to.alert
assert validateText in alert.text
sleep(5)
alert.accept()

# Negative case
driver.find_element_by_id("confirmbtn").click()
# validateText = driver.find_element_by_xpath("//input[@value='Confirm']").text
# assert validateText in alert.text
sleep(5)
alert.dismiss()
