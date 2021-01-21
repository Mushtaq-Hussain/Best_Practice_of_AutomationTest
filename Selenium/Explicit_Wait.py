from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time


class ExplicitWait():

    def test(self):

        driver = webdriver.Chrome(executable_path=r"C:\Users\mushtaq.hussain\PycharmProjects\Selenium\driver\chromedriver.exe")
        driver.maximize_window()
        print("Browser maximized")
        driver.get("https://www.expedia.com/?pwaLob=wizard-flight-pwa")
        print("URL Has been accessed")
        driver.implicitly_wait(2)

        leaveFrom = driver.find_element(By.CLASS_NAME, "uitk-faux-input")
        leaveFrom.send_keys("SFO")
        driver.find_element(By.XPATH, "//strong[contains(text(),'San Francisco (SFO - San Francisco Intl.)')]").click()

        goto = driver.find_element(By.XPATH, "//div[@id='location-field-leg1-destination-menu']//button[@class='uitk-faux-input']")
        goto.send_keys("NYC")
        driver.find_element(By.XPATH, "//strong[contains(text(),'New York (NYC - All Airports)')]").click()

        # Select Departure Date
        depDate = driver.find_element(By.ID, "d1-btn")
        depDate.click()
        driver.find_element(By.XPATH,"//div[@class='uitk-calendar']//div[1]//table[1]//tbody[1]//tr[4]//td[1]//button[1]").click()

        # Select Returnning Date
        driver.find_element(By.XPATH,"//td[@class='uitk-new-date-picker-day-number end endSelected']//button[@class='uitk-new-date-picker-day selected edge']").click()
        driver.find_element(By.XPATH,"//button[@class='uitk-button uitk-button-small uitk-button-has-text uitk-button-primary uitk-flex-item uitk-flex-shrink-0 dialog-done']").click()

        # Click on Search button
        driver.find_element(By.XPATH,"//button[@class='uitk-button uitk-button-large uitk-button-fullWidth uitk-button-has-text uitk-button-primary']").click()

        wait = WebDriverWait(driver, 20, poll_frequency= 1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//input[@id='stopFilter_stops-0']")))
        element.click()
        time.sleep(2)
        driver.quit()


ff = ExplicitWait()
ff.test()
