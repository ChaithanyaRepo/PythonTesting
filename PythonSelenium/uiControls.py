from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver")

driver.get("https://www.flipkart.com/")
driver.find_element_by_xpath("//input[@class='_2zrpKA _1dBPDZ']").send_keys("chaitanyab94@gmail.com")
sleep(2)
driver.find_element_by_xpath("//input[@class='_2zrpKA _3v41xv _1dBPDZ']").send_keys("December13!")
sleep(2)
driver.find_element_by_css_selector("button[class*='_2AkmmA _1LctnI _7UHT_c']").click()
sleep(2)
# sandals = driver.find_element_by_xpath("//input[@type='text']").send_keys("Sandals")
# print(sandals)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if(checkbox.get_attribute("value")) == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        assert checkbox.is_enabled()

# All the radio button can not be selected at once
# Selecting radio button using for loop
# radiobuttons = driver.find_elements_by_css_selector("input[type*='radio']")
# radiobuttons = driver.find_elements_by_name("radioButton")
# print(len(radiobuttons))
# for radiobutton in radiobuttons:
#     radiobutton.click()
#     assert radiobutton.is_enabled()
#     assert radiobutton.is_selected()

# Radibutton selection using index
radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_enabled()

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")

assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("show-textbox").click()
assert driver.find_element_by_id("displayed-text").is_displayed()
