from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def actionchains(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(ES.element_to_be_clickable(locator), message=f'Not found {locator}')
        ActionChains(self.driver).move_to_element(element)
        return ActionChains(self.driver).context_click(element)

    def find_element_pb(self, time=20):
        LOCATOR_DIARY_PB = (By.XPATH, '//div[@class="progress-bar"]')
        return WebDriverWait(self.driver, time).until(ES.invisibility_of_element_located(LOCATOR_DIARY_PB), message='Not found element progress bar')

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(ES.presence_of_element_located(locator), message=f'Not found {locator}')

    def find_clickable_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(ES.element_to_be_clickable(locator), message=f'Not found {locator}')