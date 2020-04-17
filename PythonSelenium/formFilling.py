from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(
    executable_path='/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver')
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("input[name='name']:nth-child(2)").send_keys("Chaithanya B")
driver.find_element_by_css_selector("input[name='email']").send_keys("nayakchaithanya12@yahoo.com")
driver.find_element_by_xpath("//input[@type='password']").send_keys("Chaisush@2010")
driver.find_element_by_xpath("//input[@type='checkbox']").click()
gender = Select(driver.find_element_by_id("exampleFormControlSelect1"))
gender.select_by_visible_text("Male")
driver.find_element_by_xpath("//div/input[@value='option2']").click()
driver.find_element_by_xpath("//div/input[@name='bday']").send_keys("13/12/1994")
driver.find_element_by_css_selector("input[class*='btn-success']").click()

alertMsg = driver.find_element_by_css_selector("div[class*='alert-success']").text
assert ("Success" in alertMsg)

driver.close()