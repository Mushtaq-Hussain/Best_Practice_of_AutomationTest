from selenium import webdriver
import time


class ReadList():

    def test(self):

        driver = webdriver.Chrome(executable_path=r"C:\Users\mushtaq.hussain\PycharmProjects\Selenium\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        time.sleep(2)
        listele = driver.find_element_by_id("product")
        data = listele.find_elements_by_tag_name("tr")
        for item in data:
            text = item.text
            print(text)
        print("elements has been founded and printed") 
        driver.quit()


ff = ReadList()
ff.test()
