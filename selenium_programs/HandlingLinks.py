from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.wikipedia.org/")
driver.maximize_window()

# links = driver.find_elements(By.TAG_NAME,'a')
# print('The number of links available in the page are:',len(links))
# for link in links:
#     print("The text is:",link.text,'----URL is: '+link.get_attribute('href'))

print('-------printing hyperlinks---------------')
other_projects_block=driver.find_element(By.CLASS_NAME,'other-projects')
block_links=other_projects_block.find_elements(By.TAG_NAME,'a')
print('the length of the block hyperlinks is:',len(block_links))
# fetching the text value from a block using index value
print('the first link is----------:',block_links.__getitem__(0).text)
for link in block_links:
    print("The text is:",link.text,'---URL is: '+link.get_attribute('href'))