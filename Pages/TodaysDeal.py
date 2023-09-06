from selenium.webdriver.common.by import By
from utilities.CommonFunction import CommonFunction

class TodaysDeal:

    def __init__(self, driver):
        self.driver = driver
        self.cf = CommonFunction(self.driver)

    locator_navigate_to_todays_deal = (By.PARTIAL_LINK_TEXT, "Today's Deals")
    locator_item_from_deal = (By.XPATH, "//div[@data-testid = 'grid-deals-container']/div[1]/div/div/a/div/div/img")
    Locator_add_to_cart_button = (By.ID, "add-to-cart-button")
    locator_verify_added_to_cart = (By.XPATH, "//span[@class='a-size-medium-plus a-color-base sw-atc-text a-text-bold']")

    def navigate_to_todays_deal_tab(self):
        self.cf.wait_and_click(self.locator_navigate_to_todays_deal)

    def select_item_from_the_list(self):
        self.cf.wait_and_click(self.locator_item_from_deal)

    def add_item_to_cart(self):
        self.cf.wait_and_click(self.Locator_add_to_cart_button)

    def verify_item_added_to_cart(self):
        self.cf.verify_page(self.locator_verify_added_to_cart,"Added to Cart")
