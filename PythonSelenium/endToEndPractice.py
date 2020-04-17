from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(
    executable_path='/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver')
driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_link_text("Shop").click()
driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
# //div[@class='card h-100']/div/h4/a
# product = //div[@class='card h-100']
for product in products:
    productNamePg1 = product.find_element_by_xpath("div/h4/a").text
    if productNamePg1 == "Blackberry":
        # Add item to card
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class*=btn]").click()
productNamePg2 = driver.find_element_by_link_text("Blackberry").text

# Ensuring same product added to cart
assert productNamePg1 == productNamePg2

# Adding another item to cart
driver.find_element_by_css_selector("input[type='number']").clear()
driver.find_element_by_css_selector("input[type='number']").send_keys("2")

# Forwarding to checkout page
driver.find_element_by_css_selector("button[class*=btn-success]").click()

# Selecting delivery location
driver.find_element_by_css_selector("input[class*='validate']").send_keys("India")

# Waiting to location name to load
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "India")))
countries = driver.find_elements_by_link_text("India")
for country in countries:
    # print(country.text)
    if country.text == "India":
        country.click()
        break
# driver.find_element_by_link_text("India").click()

# Agree to T&C
driver.find_element_by_css_selector("div[class*='checkbox']").click()
statusCheck = driver.find_element_by_css_selector("div[class*='checkbox']").is_enabled()
assert True == statusCheck
# driver.find_element_by_xpath("//div[contains(@class,'checkbox')]").click()
# statusCheck = driver.find_element_by_xpath("//div[contains(@class,'checkbox')]").is_enabled()
# assert True == statusCheck


# Proceed to next step
driver.find_element_by_css_selector("input[type='submit']").click()
# driver.find_element_by_css_selector("input[class*='btn']").click()
# driver.find_element_by_xpath("//input[contains(@class,'btn-lg')]").click()
# driver.find_element_by_xpath("//input[contains(@class,'btn')]").click()


# Wait until item visible
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[class*='alert']")))
alertMsg = driver.find_element_by_xpath("//div[contains(@class,'alert')]").text
# print(alertMsg)

# Check the alert message
assert "Success! Thank you!" in alertMsg

# Capturing the current screen
# driver.get_screenshot_as_png()
# driver.get_screenshot_as_file("screen.png")
# driver.get_screenshot_as_base64()
# driver.save_screenshot("screenCapture.png")

driver.close()
