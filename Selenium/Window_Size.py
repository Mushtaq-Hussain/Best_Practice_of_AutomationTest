from selenium import webdriver
from selenium.webdriver.common.by import By


class windowsize():

    def test(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\mushtaq.hussain\PycharmProjects\Selenium\driver\chromedriver.exe")
        driver.maximize_window()
        #driver.get("https://letskodeit.teachable.com/p/practice")
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")
        driver.implicitly_wait(2)

        Height = driver.execute_script("return window.innerHeight;")
        Width = driver.execute_script("return window.innerWidth;")
        print("Height :" + str(Height))
        print("Width :" + str(Width))

ff = windowsize()
ff.test()