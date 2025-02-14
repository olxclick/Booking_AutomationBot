from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://booking.com"

def wait_for_element(self, by, value, timeout=10):
    """Wait for an element to be present and return the element."""
    return WebDriverWait(self, timeout).until(  # <-- Use self directly
        ec.presence_of_element_located((by, value))
    )

def wait_for_elements(self, by, value, timeout=10):
    """Wait for a list of elements to be present and return them."""
    return WebDriverWait(self, timeout).until(  # <-- Use self directly
        ec.presence_of_all_elements_located((by, value))
    )
