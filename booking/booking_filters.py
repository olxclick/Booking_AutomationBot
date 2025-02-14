from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import booking.constants as constants


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def star_filter(self, *stars):
        # Use the constants functions with self.driver
        constants.wait_for_element(self.driver, By.CSS_SELECTOR, '[data-testid="filters-group"]')

        for s_star in stars:
            # Re-fetch the child elements every time to avoid stale references
            star_child_elements = constants.wait_for_elements(self.driver, By.CSS_SELECTOR, '*')

            # Retry logic: Keep trying until you click the correct element
            clicked = False
            while not clicked:
                for star_element in star_child_elements:
                    try:
                        if str(star_element.get_attribute('innerHTML')).strip() == f'{s_star} stars':
                            star_element.click()
                            print(f"Clicked on {s_star} stars filter.")
                            clicked = True  # Successfully clicked, stop retrying
                            break  # Exit inner loop and continue with the next filter
                    except StaleElementReferenceException:
                        print(f"Element for {s_star} stars is stale. Retrying...")
                        star_child_elements = constants.wait_for_elements(self.driver, By.CSS_SELECTOR, '*')
                        break  # Break to reattempt the whole process

    def lowest_price(self):
        sort_element = constants.wait_for_element(self.driver, By.CSS_SELECTOR, '[data-testid="sorters-dropdown-trigger"]')
        sort_element.click()

        low_price_element = constants.wait_for_element(self.driver, By.CSS_SELECTOR, 'button[data-id="price"]')
        low_price_element.click()