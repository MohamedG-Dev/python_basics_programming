# selenium version used currently is Version: 4.27.1
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.ID,'dropdown-class-example').send_keys("Option2")

# The below code is the prime example of that the send_keys() method doesn't works 100%
#
driver.get("https://www.wikipedia.org/")
time.sleep(5)
# driver.find_element(By.ID,'searchLanguage').send_keys("Eesti")
# for the above code, when Eesti is given via send keys, then the value should be displayed as ET
# but instead it displays ES

language_dropdown=driver.find_element(By.ID,'searchLanguage')
dropdown = Select(language_dropdown)
# dropdown.select_by_visible_text('Eesti')
# dropdown.select_by_value('hi')
dropdown.select_by_index(5)

options=driver.find_elements(By.TAG_NAME,'option')
for option in options:
    print('option value is-',option.get_attribute('lang'))

print('Total dropdown values are:',len(options))