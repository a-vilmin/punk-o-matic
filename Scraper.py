from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Scraper():

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

    def get_files(self, site):
        self.driver.get(site)
        body = self.driver.find_element(By.CSS_SELECTOR, "body")
        print(body.get_attribute('class'))

        # Wait for page to load
        sleep(5)
        i = body.find_element_by_xpath("//div[@id='main']//ol[@id='items']")

        items = i.find_elements_by_xpath("//li[@class='item']")

        for each in items:
            print(str(each.get_attribute('class')))

if __name__ == '__main__':

    chrome = './chromedriver'
    site = 'https://whendeathwontsolveyourproblem.blogspot.com/'

    test = Scraper(chrome)
    test.get_files(site)
