# selenium version used currently is Version: 4.27.1

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException

# driver=webdriver.Chrome(keep_alive=ChromeDriverManager().install())
driver = webdriver.Chrome()
# driver=webdriver.Edge()
# driver=webdriver.Firefox()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# Code for implicit wait
driver.implicitly_wait(10)
# driver.find_element_by_name("name").send_keys("Thomas")
time.sleep(3)
#the time.sleep() method is used in this program just view the data entered in to the application.
# Since the speed is fast unable to view the data entered during execution
# time.sleep() is a method used to provide to apply waits for the execution of program or delays the execution for certain amount of time.

# Explicit Wait code
explicit_Wait=WebDriverWait(driver,10)
# explicit_Wait.until(EC.presence_of_element_located((By.NAME,"name"))).send_keys("Thomas")
# Another way to use it is
# element= explicit_Wait.until(EC.presence_of_element_located((By.NAME,"name")))
# element.send_keys("Thomas")
# Another example of Explicit WebDriver wait is - this is as per the latest verison and as mentioned in the Selenium Dev website
# username_element=driver.find_element(By.NAME,"name")
# explicit_Wait.until(lambda d:username_element.is_displayed())
# username_element.send_keys("Peaky")

# Fluent wait Code
errors_exceptions=[NoSuchElementException,ElementNotVisibleException]
fluent_Wait=WebDriverWait(driver,timeout=10,poll_frequency=1,ignored_exceptions=errors_exceptions)
# fluent_Wait.until(EC.presence_of_element_located((By.NAME,"name"))).send_keys("Rock")
# Another way for fluent wait is - this is as per the latest version and as mentioned in the Selenium Dev website
username_element=driver.find_element(By.NAME,"name")
fluent_Wait.until(lambda d:username_element.send_keys("Arthur") or True)


time.sleep(2)
driver.find_element(By.NAME,'email').send_keys("thomas@gmail.com")
time.sleep(2)
driver.find_element(By.ID,'exampleInputPassword1').send_keys("thomas123")
time.sleep(2)
