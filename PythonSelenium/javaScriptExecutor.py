# JavaScript DOM can access any elements on web page just like  how selenium does
# Using Selenium we can execute Javascript code
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver')
driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_xpath("//form/div[1]/input[contains(@class,'ng-invalid')]").send_keys("Good Morning")
driver.find_element_by_name("name").send_keys("Good Morning")
# This API returns text which are present during page loading
# This API can not use to read text entered by user
print(driver.find_element_by_name("name").text)
# API returns the text present in the element specified
print(driver.find_element_by_name("name").get_attribute("value"))
# Java Script Executor
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopButton = driver.find_element_by_css_selector("a[href*='shop']:nth-child(1)")
driver.execute_script("arguments[0].click();", shopButton)
# Scrolling a page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")