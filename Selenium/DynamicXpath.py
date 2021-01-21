from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DynamicXpath():

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
        email.send_keys("test@email.com")
        pwd = driver.find_element(By.ID, "user_password")
        pwd.send_keys("abcabc")
        loginbtn = driver.find_element(By.NAME, "commit")
        loginbtn.click()
        print("User login successfully")
        #Read Captcha
        time.sleep(20)

        #Search courses
        searchbox = driver.find_element(By.ID, "search-courses")
        searchbox.send_keys("JavaScript")
        clicksearchBtn = driver.find_element(By.XPATH, "//i[@class='fa fa-search']")
        clicksearchBtn.click()
        time.sleep(2)
        print("Required has been searched")

        #Select Course
        course = "//div[contains(@class,'course-listing-title') and contains(text(), '{0}')]"
        courselocator = course.format("JavaScript for beginners")
        print("Dynamic Xpath has been created")
        courseElement = driver.find_element(By.XPATH,courselocator)
        courseElement.click()
        print("Element found by Dynamic Xpath")
        time.sleep(2)
        driver.quit()


ff = DynamicXpath()
ff.test()