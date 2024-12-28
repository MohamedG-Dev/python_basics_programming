from abc import ABC, abstractclassmethod
class WebDriver(ABC):

    @abstractclassmethod
    def click(self):
        pass
# obj=WebDriver()
# obj.click()

class ChromeDriver(WebDriver):

    def capturing_screenshot(self):
        print("Capturing screenshot in chrome")
    def click(self):
        print("Clicking in chrome")

class Firefox(WebDriver):

    def capturing_screenshot(self):
        print("capturing screenshot in the firefox")
    def click(self):
        print("clicking in firfefox")

obj =ChromeDriver()
obj.capturing_screenshot()
obj.click()
obj1=Firefox()
obj1.capturing_screenshot()
obj1.click()