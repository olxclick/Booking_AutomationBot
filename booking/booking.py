import os
from booking.booking_filters import BookingFiltration
import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/Users/joaol/Documents/chromedriver-win64"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)

    def land_first_page(self):
        self.get(const.BASE_URL)

    def close_cookie_banner(self):
        try:
            # Wait for the cookie banner and click the "Accept" button
            cookie_accept_button = const.wait_for_element(self, By.ID, "onetrust-accept-btn-handler")
            cookie_accept_button.click()
            print("Clicked on the cookie accept button.")
        except:
            print("No cookie banner found.")

    def change_currency(self, currency='U.S. Dollar'):
        currency_element = self.find_element(By.XPATH, "//button[@data-testid='header-currency-picker-trigger']")
        currency_element.click()

        # Wait for the currency element and click it
        wanted_currency = const.wait_for_element(self, By.XPATH, f"//button[.//span[contains(text(), '{currency}')]]")
        wanted_currency.click()
        print(f'Clicked the {currency} button')

    def select_place(self, location='Tokyo'):
        field = self.find_element(By.ID, ':rh:')
        field.clear()
        field.send_keys(location)

        # Wait for results to load
        const.wait_for_elements(self, By.XPATH, "//li[@role='option']")

        select_loc = const.wait_for_element(self, By.XPATH, f"//li[div//div[contains(text(), '{location}')]]")
        select_loc.click()
        print(f"Clicked the location: {location}")

    def select_date(self, check_in, check_out):
        check_in_element = const.wait_for_element(self, By.CSS_SELECTOR, f"span[data-date='{check_in}']")
        check_in_element.click()
        print(f'Selected {check_in} for check-in')

        check_out_element = const.wait_for_element(self, By.CSS_SELECTOR, f"span[data-date='{check_out}']")
        check_out_element.click()
        print(f'Selected {check_out} for check-out')

    def add_adult(self, n):
        # Find the button to add an adult and click it
        add_button = const.wait_for_element(self, By.CSS_SELECTOR, "button.f4d78af12a")
        for _ in range(n):
            add_button.click()

    def remove_adult(self, n):
        # Find the button to remove an adult and click it
        remove_button = const.wait_for_element(self, By.CSS_SELECTOR, "button[aria-hidden='true'][class*='f38b6daa18']")
        for _ in range(n):
            remove_button.click()

    def select_guests(self, number_of_adults):
        guest_element = const.wait_for_element(self, By.CSS_SELECTOR, "button[data-testid='occupancy-config']")
        guest_element.click()

        adult_value_element = const.wait_for_element(self, By.ID, "group_adults")
        adult_value = int(adult_value_element.get_attribute('value'))  # Count of adults

        if adult_value > number_of_adults:
            self.remove_adult(adult_value - number_of_adults)
        elif adult_value < number_of_adults:
            self.add_adult(number_of_adults - adult_value)

    def click_search(self):
        search_button = const.wait_for_element(self, By.CSS_SELECTOR, "button[type='submit']")
        search_button.click()

    def apply_filters(self):
        filters = BookingFiltration(self)
        filters.star_filter(3, 4, 5)
        filters.lowest_price()
