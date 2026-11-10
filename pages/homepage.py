from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get("https://www.demoblaze.com/index.html")


    def click_galaxy_s6(self):
        galaxy_s6 = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Samsung galaxy s6")
        galaxy_s6.click()


    def click_monitor(self):
        monitor_link = self.browser.find_element(By.XPATH, "//a[@onclick=\"byCat('monitor')\"]")
        monitor_link.click()


    def click_product_count(self, count):
        monitors = self.browser.find_elements(By.CSS_SELECTOR, value='.card')
        assert len(monitors) == count

