from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class DragAndDrop():

    def test(self):
        driver = webdriver.Chrome(executable_path= r"C:\Users\mushtaq.hussain\PycharmProjects\Selenium\driver\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://jqueryui.com/droppable/")
        driver.implicitly_wait(2)
        # First move to iFram
        driver.switch_to.frame(0)

        dragelement = driver.find_element(By.ID, "draggable")
        dropelement = driver.find_element(By.ID, "droppable")
        try:
            actions = ActionChains(driver)
            # actions.drag_and_drop(dragelement, dropelement).perform()
            actions.click_and_hold(dragelement).move_to_element(dropelement).release().perform()
            print("Drag and Drop successfully")
        except:
            print("Drag and Drop failed")

AA = DragAndDrop()
AA.test()