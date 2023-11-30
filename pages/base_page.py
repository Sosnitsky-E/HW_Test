from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:

    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link

    def open_page(self):
        self.driver.get(self.link)

    def go_to_element(self, element):
        """
        Scroll the page to the selected element so that the element becomes visible to the user.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def element_is_present(self, locator, timeout=5):
        """
        Expects to check that the element is present in the DOM tree, but not necessarily,
         what is visible and displayed on the page.
         Returns WebElement.
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_visible(self, locator, timeout=5):
        """
        Waiting for verification that the element present in DOM
        """
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def action_move_to_element_click(self, locator):
        """
        This method moves the mouse cursor to the center of the selected element.
        Perform a click action without navigating to a new page
        """
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def element_is_clickable(self, element, timeout=5):
        """
        Expects to check that the element is clickable
         Returns WebElement.
        """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(element))

    def get_actual_url_of_current_page(self):
        """
        This method allows to get URL of the current page
        """
        actual_url = self.driver.current_url
        return actual_url

    def fill_in_field(self, locator, value):
        """This method fills in a specified field with provided value"""
        input_field = self.element_is_clickable(locator)
        input_field.click()
        input_field.clear()
        input_field.send_keys(value)
        return input_field

    def get_text(self, locator):
        """This method check if the element is visible
        Returns text of the element."""
        return self.element_is_visible(locator, 20).text

