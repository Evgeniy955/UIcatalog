from time import sleep

from trainee_auto_tests.functions.func import Functions
from trainee_auto_tests.locators import locators


class Byiphone(Functions):


    def url_address(self):
        self.get_url('https://www.apple.com/iphone/buy')

    def click_iphone13pro(self):
        self.tap_on_element(locators.iphone13pro)

    def click_buy_button(self):
        self.tap_on_element(locators.buy_button)

    def click_iphone13pro_max(self):
        self.tap_on_element(locators.iphone13pro_max)
        sleep(1)

    def click_color(self):
        self.tap_on_element(locators.color)
        sleep(1)

    def click_memory_device(self):
        self.tap_on_element(locators.memory_device)
        sleep(1)

    def click_connect_later(self):
        self.tap_on_element(locators.connect_later)

    def click_no_smartphone_to_trade(self):
        self.tap_on_element(locators.no_smartphone_to_trade)
        sleep(1)

    def click_payment_option(self):
        self.tap_on_element(locators.payment_option)
        sleep(1)

    def click_one_time_payment(self):
        self.tap_on_element(locators.one_time_payment)

    def click_add_to_bag(self):
        self.tap_on_element(locators.add_to_bag)
        sleep(3)

    def assert_bag(self):
        self.check_text('iPhone 13 Pro Max 512GB Silver', locators.review_bag)
