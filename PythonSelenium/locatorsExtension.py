from selenium import webdriver
from time import sleep

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver')
driver.get("https://www.amazon.in/")

# Generating CSS using ID
driver.find_element_by_css_selector("input#twotabsearchtextbox").send_keys("Teddy")
sleep(5)
driver.find_element_by_css_selector("#twotabsearchtextbox").clear()
sleep(2)
driver.find_element_by_css_selector("a.nav-logo-link").click()
sleep(2)
# driver.get("https://www.google.com/")
# The link text works only when the tag name is "a" for others we can't use it
# print(driver.find_element_by_link_text("Gmail").text)
# //tagname[text()='value']
# driver.find_element_by_xpath("//a[text()='Images']").click()

# driver.get("https://www.flipkart.com/")
# driver.find_element_by_xpath("//div[@class='_39M2dM JB4AMj']/input").send_keys("chaitanyab94@gmail.com")
# sleep(1)
# driver.find_element_by_css_selector("div[class='_39M2dM JB4AMj'] input").send_keys("December13!")

dropdown = Select(driver.find_element_by_css_selector("select[id='searchDropdownBox']"))
dropdown.select_by_visible_text("Watches")
sleep(5)
dropdown.select_by_index("13")
sleep(5)
dropdown.select_by_value("search-alias=electronics")

message = driver.find_element_by_css_selector("input[id='twotabsearchtextbox']").send_keys("Girls watches")

# Adding validation assertions in program
assert "watches" in message
