from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30, 0.3)

    # Ожидание элемента на странице
    def is_visible_css(self, locator) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))

    def is_visible_id(self, locator) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located((By.ID, locator)))

    # Отсутствие элемента на странице
    def is_invisible_css(self, locator) -> WebElement:
        return self.wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, locator)))

    def is_invisible_class(self, locator) -> WebElement:
        return self.wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, locator)))

    # Нажатие на элемент
    def click_button(self, locator):
        return self.is_visible_css(locator).click()

    # Присутствие элемента
    def is_visible_class(self, locator) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, locator)))

    def is_visible_xpath(self, locator) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, locator)))

    def is_visible_tag(self, locator) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located((By.TAG_NAME, locator)))


    def are_visible_class(self, locator) -> WebElement:
        return self.wait.until(ec.visibility_of_all_elements_located((By.CLASS_NAME, locator)))







