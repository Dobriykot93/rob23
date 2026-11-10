import time
from pages.homepage import Homepage
from pages.product import Product

def test_open_s6(browser):
    homepage = Homepage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product = Product(browser)
    product.check_title_is("Samsung galaxy s6")

def test_two_monitors(browser):
    homepage = Homepage(browser)
    homepage.open()
    #browser.get("https://www.demoblaze.com/")
    #monitor_link = browser.find_element(By.XPATH, "//a[@onclick=\"byCat('monitor')\"]")
    #monitor_link.click()
    homepage.click_monitor()
    time.sleep(3)
    #monitors = browser.find_elements(By.CSS_SELECTOR, value='.card')
    #assert len(monitors) == 2
    homepage.click_product_count(2)


