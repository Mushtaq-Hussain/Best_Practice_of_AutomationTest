from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GenericScreenShotMethod():

    def test(self):

        driver = webdriver.Chrome(executable_path=r"C:\Users\mushtaq.hussain\PycharmProjects\Selenium\driver\chromedriver.exe")
        driver.maximize_window()
        print("Browser maximized")
        driver.get("https://letskodeit.teachable.com/")
        print("URL Has been accessed")
        time.sleep(2)


        #Perform Login
        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(2)
        email = driver.find_element(By.ID, "user_email")
        email.send_keys("abc@email.com")
        pwd = driver.find_element(By.ID, "user_password")
        pwd.send_keys("abc")
        loginbtn = driver.find_element(By.NAME, "commit")
        loginbtn.click()
        self.takescreenshot(driver)

    def takescreenshot(self, driver):

        fileName = str(round(time.time() * 1000)) + ".png"
        screnshotdirectory = "ScreenShots/"
        destinationfile = screnshotdirectory + fileName
        try:
            driver.save_screenshot(destinationfile)
            print("ScreenShot saved in to dirctory")
        except NotADirectoryError:
            print("Not a directory issue")


ff = GenericScreenShotMethod()
ff.test()