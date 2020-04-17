from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver")
driver.get("https://the-internet.herokuapp.com/frames")

driver.find_element_by_link_text("iFrame").click()
print(driver.find_element_by_tag_name("h3").text)
# frameName frameId frameIndex
driver.switch_to.frame("mce_0_ifr")
print(driver.find_element_by_xpath("//body/p").text)
# driver.find_element_by_css_selector("body#tinymce").clear()
# driver.find_element_by_css_selector("body.mce-content-body").clear()
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("Hello Good Morning ;-) :-)")
# To come out of frames
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)
