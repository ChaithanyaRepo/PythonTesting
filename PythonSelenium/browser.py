from selenium import webdriver
from time import sleep

# driver object
# browser exposes a executable file and we have to invoke it

# Chrome Driver
# driver = webdriver.Chrome(executable_path='/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver')

# Firefox Driver
driver = webdriver.Firefox(executable_path='/home/chaitanya/Documents/software/drivers/geckodriver-v0.26.0-linux64/geckodriver')

driver.maximize_window()
driver.get("https://accounts.google.com/signin")
print(driver.title)
print(driver.current_url)
# sleep(5)

driver.get("https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.delete_all_cookies()
print(driver.title)
print(driver.current_url)
# sleep(5)

driver.back()
driver.refresh()
# sleep(5)

driver.close()
# driver.quit()
