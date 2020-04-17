from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver")
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()
# Capturing all the opened windows
windows = driver.window_handles
# print(windows)
# Switching to child window
driver.switch_to.window(windows[1])
# print(driver.find_element_by_xpath("//div/h3").text)
# Finding the element using tag name
print(driver.find_element_by_tag_name("h3").text)
assert "New Window" == driver.find_element_by_tag_name("h3").text

driver.close()
# Switching back to parent window
driver.switch_to.window(windows[0])
print(driver.find_element_by_tag_name("h3").text)
assert "Opening a new window" == driver.find_element_by_tag_name("h3").text
