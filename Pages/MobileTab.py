from selenium.webdriver.common.by import By
from utilities.CommonFunction import CommonFunction


class MobileTab:

    def __init__(self, driver):
        self.driver = driver
        self.cf = CommonFunction(self.driver)

    locator_navigate_to_Mobiles_tab = (By.LINK_TEXT, "Mobiles")
    locator_select_mobile_from_list = (By.XPATH, "(//ol[@class='sl-sobe-carousel-viewport-row-inner'])[2]/li[2]")
    locator_image_to_hover = (By.ID, "imgTagWrapperId")
    locator_zoomed_image = (By.ID, "zoomWindow")

    def navigate_to_mobile_tab(self):
        self.cf.wait_and_click(self.locator_navigate_to_Mobiles_tab)

    def select_mobile_from_list(self):
        self.cf.wait_and_click(self.locator_select_mobile_from_list)

    def mouse_over_image(self):
        self.cf.wait_and_hover(self.locator_image_to_hover)

    def verify_image(self):
        self.cf.verify_image_present(self.locator_zoomed_image)
