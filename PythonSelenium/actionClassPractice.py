from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver")
driver.get("https://www.familysearch.org/en/")
driver.maximize_window()

actionChain = ActionChains(driver)
# actionChain.move_to_element(driver.find_element_by_css_selector("nav[id='primaryNav'] div:nth-child(2) button")).click().perform()
actionChain.move_to_element(driver.find_element_by_xpath("//button[@class='primary-nav-text nav-menu-trigger'][contains(text(),'Search')]")).click().perform()

# actionChain.move_to_element(driver.find_element_by_css_selector("ul[id='search'] li:nth-child(4)")).click().perform()
# actionChain.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()
driver.find_element_by_link_text("Genealogies").click()
# actionChain.move_to_element(driver.find_element_by_xpath("//ul[@id='search']/li[4]")).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver.php")

actionChain = ActionChains(driver)
# Context click i.e right click
# actionChain.context_click(driver.find_element_by_id("double-click")).perform()
# Performing the double click
actionChain.double_click(driver.find_element_by_id("double-click")).perform()

alert = driver.switch_to.alert
text = alert.text
# Clicking OK in the pop-up
assert text == "You double clicked me!!!, You got to be kidding me"
alert.accept()

# driver.refresh()
# driver.find_element_by_id("page-top").click()

# WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, "sub-menu")))
# Hover Action
# actionChain.move_to_element(driver.find_element_by_id("sub-menu")).perform()

# IS DISPLAYED
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_id("displayed-text").is_displayed()
sleep(5)
driver.find_element_by_id("hide-textbox").click()
driver.find_element_by_id("displayed-text").is_displayed()
sleep(5)
driver.find_element_by_id("show-textbox").click()
driver.find_element_by_id("displayed-text").is_displayed()

driver.close()