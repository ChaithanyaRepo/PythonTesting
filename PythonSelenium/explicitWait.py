from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

vegListPg1 = []
vegListPg2 = []
vegListExpected = ['Cauliflower - 1 Kg', 'Carrot - 1 Kg', 'Capsicum', 'Cashews - 1 Kg']
vegListActual = []

driver = webdriver.Chrome(executable_path="/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Expected and actual comparision
driver.find_element_by_class_name("search-keyword").send_keys("ca")
sleep(5)
# wait = WebDriverWait(driver, 20)
# wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "product-name")))
vegetables = driver.find_elements_by_xpath("//div/div/h4[@class='product-name']")
# vegetables = driver.find_elements_by_css_selector("h4.product-name")
# vegetables = driver.find_elements_by_xpath("//h4[@class='product-name']")
for vegetable in vegetables:
    vegListActual.append(vegetable.text)
    print(vegetable.text)
print("Actual", vegListActual)
print("Expected", vegListExpected)
assert vegListActual == vegListExpected

driver.find_element_by_css_selector("input.search-keyword").clear()
# driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
# Python wait period
sleep(2)
# Explicit wait
wait = WebDriverWait(driver, 2)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='products']/div")))

count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
# print(count)
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    # Optimized code for grabbing th vegetable names
    # print(button.find_element_by_xpath("//div[@class='product-action']/button/parent::div/parent::div/h4").text)
    # Collecting the vegetable names from first page
    vegListPg1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print("First List", vegListPg1)

# Cart open
driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

# sleep(2)
# Promo code enter
# Explicit wait
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "promoCode")))
# Grab the vegetable names for comparision
vegetables = driver.find_elements_by_css_selector("p.product-name")
for vegetable in vegetables:
    # Collecting the vegetable names form second page
    vegListPg2.append(vegetable.text)
print("Second List", vegListPg2)

# Comparing vegetable names from first and second page
assert vegListPg1 == vegListPg2

amtBfrDiscnt = driver.find_element_by_css_selector("span.discountAmt").text
print("Before Discount", amtBfrDiscnt)
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()

# Explicit wait
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
# print(driver.find_element_by_css_selector("span.promoInfo").text)

amtAfrDiscnt = driver.find_element_by_css_selector("span.discountAmt").text
print("After Discount", amtAfrDiscnt)

# Comparing two amounts
assert float(amtAfrDiscnt) < float(amtBfrDiscnt)

# Summing the total
sum = 0
amounts = driver.find_elements_by_xpath("//table/tr/td[5]/p")
for amount in amounts:
    sum += int(amount.text)
totAmt = int(driver.find_element_by_class_name("totAmt").text)
print("Total Amount", totAmt)
assert totAmt == sum

driver.find_element_by_xpath("//button[text()='Place Order']").click()

# Country selection
dropdown = Select(driver.find_element_by_xpath("//div/select"))
dropdown.select_by_visible_text("India")
# dropdown.select_by_value("value=India")

# Terms and Conditions
driver.find_element_by_css_selector("input.chkAgree").click()

# Procees
driver.find_element_by_xpath("//div/button").click()
