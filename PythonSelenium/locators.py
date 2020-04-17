from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver')
# driver = webdriver.Firefox(executable_path='/home/chaitanya/Documents/software/drivers/geckodriver-v0.26.0-linux64/geckodriver')
driver.get("https://www.flipkart.com/")
sleep(1)
# driver.find_element_by_css_selector("input[class='_2zrpKA _1dBPDZ']").send_keys("chaitanyab94@gmail.com")
driver.find_element_by_xpath("//input[@class='_2zrpKA _1dBPDZ']").send_keys("chaitanyab94@gmail.com")
# driver.find_element_by_name("identifier").send_keys("chaitanyab94@gmail.com")
# driver.find_element_by_css_selector("span[class='CwaK9']").click()
sleep(1)
driver.find_element_by_css_selector("input[class='_2zrpKA _3v41xv _1dBPDZ']").send_keys("December13!")
# driver.find_element_by_name("password").send_keys("December13!")
# driver.find_element_by_css_selector("button[class='_2AkmmA _1LctnI _7UHT_c']").click()
driver.find_element_by_css_selector("[class*='_1LctnI _7UHT_c']").click()

# driver.find_element_by_name("identifier").send_keys("chaitanyab94@gmail.com")
# driver.find_element_by_class_name("CwaK9").click()
# sleep(1)
# driver.find_element_by_name("password").send_keys("Nayak@123")
# driver.find_element_by_class_name("CwaK9").click()

# Copying the text from web page
# print(driver.find_element_by_class_name("oZoRPi").text)
# print(driver.find_element_by_css_selector("a[class='oZoRPi']").text)
# print(driver.find_element_by_xpath("//a[@class='oZoRPi']").text)
sleep(1)
# XPath with regular expression
# print(driver.find_element_by_xpath("//*[contains(@class,'oZoRPi')]").text)
sleep(1)
# CSS Selector with regular expression
# print(driver.find_element_by_css_selector("[class='oZoRPi']").text)

driver.get("https://www.amazon.in/")
sleep(1)

# Generating CSS using ID
driver.find_element_by_css_selector("input#twotabsearchtextbox").click()
