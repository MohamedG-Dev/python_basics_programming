# selenium version used currently is Version: 4.27.1
# Selenium import statement
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# command to initialize the chromedriver path
# driver=webdriver.Chrome(keep_alive="C:/Users/OSAMA/Downloads/python-selenium-downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
# driver=webdriver.Chrome(keep_alive="selenium_jars/chromedriver.exe")
# driver=webdriver.Chrome(keep_alive=ChromeDriverManager().install())
# driver=webdriver.Firefox(keep_alive=GeckoDriverManager().install())
driver=webdriver.Edge(keep_alive=EdgeChromiumDriverManager().install())
# command to navigate to the url
driver.get("https://www.way2automation.com/")

# command to make the window maximize
driver.maximize_window()
driver.minimize_window()

# command to get the title
title=driver.title
print(title)

# code for assertion
assert 'Selenium' in title
# assert 'selenium' in title

# code for closing the browser
driver.close()
driver.quit()
