from selenium import webdriver
import chromedriver_autoinstaller



class Browser(object):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=chrome_options) #'C:/ChromeDriver/chromedriver.exe',
    driver.implicitly_wait(50)
    driver.set_page_load_timeout(50)

    def close(self):
        self.driver.close()

