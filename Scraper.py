from selenium import webdriver


class Scraper():

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

if __name__ == '__main__':

    chrome = './chromedriver'

    test = Scraper(chrome)
 
