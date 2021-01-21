from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ExpediaSearch():

    def test(self):

        driver = webdriver.Chrome(executable_path=r"C:\Users\mushtaq.hussain\PycharmProjects\Selenium\driver\chromedriver.exe")
        driver.maximize_window()
        print("Browser maximized")
        driver.get("https://www.expedia.com/?pwaLob=wizard-flight-pwa")
        print("URL Has been accessed")
        time.sleep(2)

        leaveFrom = driver.find_element(By.CLASS_NAME, "uitk-faux-input")
        leaveFrom.send_keys("Islamabad")
        time.sleep(2)
        driver.find_element(By.XPATH, "//strong[contains(text(),'Islamabad (ISB - Islamabad Intl.)')]").click()
        time.sleep(2)

        goto = driver.find_element(By.XPATH, "//div[@id='location-field-leg1-destination-menu']//button[@class='uitk-faux-input']")
        goto.send_keys("Canada")
        time.sleep(2)
        driver.find_element(By.XPATH, "//li[@class='uitk-typeahead-result-item has-subtext']//div[@class='is-subText truncate'][contains(text(),'Ontario, Canada')]").click()

        #Select Departure Date
        depDate = driver.find_element(By.ID, "d1-btn")
        depDate.click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='uitk-calendar']//div[1]//table[1]//tbody[1]//tr[4]//td[1]//button[1]").click()
        time.sleep(2)

        #Select Returnning Date
        driver.find_element(By.XPATH, "//td[@class='uitk-new-date-picker-day-number end endSelected']//button[@class='uitk-new-date-picker-day selected edge']").click()
        driver.find_element(By.XPATH, "//button[@class='uitk-button uitk-button-small uitk-button-has-text uitk-button-primary uitk-flex-item uitk-flex-shrink-0 dialog-done']").click()
        time.sleep(2)

        # Click on Search button
        driver.find_element(By.XPATH, "//button[@class='uitk-button uitk-button-large uitk-button-fullWidth uitk-button-has-text uitk-button-primary']").click()
        time.sleep(5)

ff = ExpediaSearch()
ff.test()

