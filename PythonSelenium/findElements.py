from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver')
driver.get("https://www.makemytrip.com/")

driver.find_element_by_id("fromCity").click()
driver.find_element_by_xpath("//input[@placeholder='From']").send_keys("Del")
sleep(2)
cities = driver.find_elements_by_css_selector("p[class*=blackText]")
print(len(cities))
for city in cities:
    # print(city.text)
    if city.text == "Deline, Canada":
        print("City got clicked")
        city.click()
        break
sleep(1)
driver.find_element_by_xpath("//p[text()='Bangkok, Thailand']").click()
