from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")

sleep(4)

count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()

# Cart open
driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
# sleep(2)
# Promo code enter
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)
# sleep(5) - python wait timer
# driver.find_element_by_xpath("//button[text()='Place Order']").click()


