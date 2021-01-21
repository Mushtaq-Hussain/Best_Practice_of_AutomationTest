from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class MouseHover():

    def test(self):
        driver = webdriver.Chrome(executable_path= r"C:\Users\mushtaq.hussain\PycharmProjects\Selenium\driver\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.implicitly_wait(2)

        driver.execute_script("window.scrollBy(0, 800);")
        element = driver.find_element(By.ID, "mousehover")
        elementToClick = "//a[contains(text(),'Top')]"
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Hover on Element")
            time.sleep(2)
            toplink = driver.find_element(By.XPATH, elementToClick)
            actions.move_to_element(toplink).click().perform()
            print("Clicked On Element")
            time.sleep(2)
        except:
            print("Hover failed on element")


SS = MouseHover()
SS.test()


