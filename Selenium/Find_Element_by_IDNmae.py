from selenium import webdriver


class FindElementByIdName():
    def test(self):
        driver = webdriver.Chrome("driver/chromedriver.exe")
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(3)

        findelementbyname = driver.find_element_by_name("enter-name")
        if findelementbyname is not None:
            print("Element founded by name")

        findelementbyid = driver.find_element_by_id("displayed-text")
        if findelementbyid is not None:
            print("Element founded by Id")


ele = FindElementByIdName()
ele.test()
