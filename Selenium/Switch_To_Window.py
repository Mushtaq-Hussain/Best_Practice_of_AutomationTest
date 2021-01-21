from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToWindow():

    def test(self):
        driver = webdriver.Chrome(executable_path= r"C:\Users\mushtaq.hussain\PycharmProjects\Selenium\driver\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.implicitly_wait(2)

        # find parent Handle => Main Handle
        parenthandle = driver.current_window_handle
        print("Current window is :" + parenthandle)

        # Find Open window button and click on it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Find all handler, there should be two handler for open window
        handles = driver.window_handles
        for handle in handles:
            print("Window Handle :" + handle)
            if handle not in parenthandle:
                driver.switch_to.window(handle)
                print("Switch to :" + handle)
                element = driver.find_element(By.ID, "search-courses")
                element.send_keys("python")
                time.sleep(2)
                driver.close()
                break
        # Switch back to Parent window
        driver.switch_to.window(parenthandle)
        print("Switch back to :" + parenthandle)
        element2 = driver.find_element(By.ID, "name")
        element2.send_keys("test successful")
        time.sleep(2)


aa = SwitchToWindow()
aa.test()