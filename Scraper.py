from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class Scraper():

    def __init__(self, driver_path, options):
        self.driver = webdriver.Chrome(executable_path=driver_path,
                                       chrome_options=options)

        self.links = set()

    def get_links(self, site):
        self.driver.get(site)
        bd = self.driver.find_element(By.CSS_SELECTOR, "body")

        # Wait for page to load
        sleep(2)
        try:
            i = bd.find_element_by_xpath("//div[@id='main']//ol[@id='items']")
            blog_entries = i.find_elements_by_xpath("//li[@class='item']")

        except NoSuchElementException:
            print("They changed the layout. Check the site's markup")

        for each in blog_entries:
            all_l = each.find_elements_by_xpath("//div[@class='separator']//a")
            for l in all_l:
                if l.text == "Download":
                    self.links.add(l.get_attribute("href"))

    def download(self):
        for site in self.links:
            if 'zippy' in site:
                self._zippy_share(site)
            elif 'bandcamp' in site:
                continue

    def _zippy_share(self, url):
        self.driver.get(url)
        sleep(1)
        try:
            link = self.driver.find_element_by_xpath("//body//div[@class='container']" +
                                                     "//div[@class='outer_main']" +
                                                     "//div[@class='inner_main']" +
                                                     "//table//tbody//tr//td//" +
                                                     "div[@id='lrbox']//div[@class='rig" +
                                                     "ht']//div//a").get_attribute('href')
            self.driver.get(link)
            sleep(4)
        except NoSuchElementException:
            print("cant find link")

if __name__ == '__main__':

    chrome = './chromedriver'
    site = 'https://whendeathwontsolveyourproblem.blogspot.com/'

    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "/home/vilmin2/Music/"}
    chromeOptions.add_experimental_option("prefs", prefs)

    test = Scraper(chrome, chromeOptions)
    test._zippy_share("http://www72.zippyshare.com/v/SUml3bXd/file.html")
