# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import logging


class Page:

    def __init__(self):
        self.driver = None
        self.wait_for_page_load()

    def set_driver(self, web_driver):
        self.driver = web_driver
        return self

    def set_value(self, locator, value):
        elem = self.get_element_by(locator)
        # force focus on element before send_keys
        elem.click()
        if elem.tag_name == 'select':
            Select(elem).select_by_value(value)
        elif elem.get_attribute('type') == 'checkbox':
            elem.click()
        else:
            elem.clear()
            elem.send_keys(value)

    def get_value(self, locator):
        elem = self.get_element_by(locator, 15)
        if elem.tag_name == 'select':
            select = Select(elem).first_selected_option
            return select.get_attribute("value")
        elif elem.tag_name in ('textarea', 'div'):
            return elem.text
        else:
            return elem.get_attribute('value')

    def get_element_by(self, by, timeout=3):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(by)
            )
        except (NoSuchElementException, TimeoutException) as err:
            # logging.error(f"Exception Type: {type(err)}")
            # logging.error(f"No such element: {(by, )}")
            return None
        return element

    def get_elements_by(self, by, timeout=3):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_all_elements_located(by)
            )
        except (NoSuchElementException, TimeoutException) as err:
            # logging.error(f"Exception Type: {type(err)}")
            # logging.error(f"No such element: {(by,)}")
            return None
        return element

    def wait_for_visible(self, locator, timeout=3):
        """ Check the element if it is visible """
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(locator)
            )
        except (NoSuchElementException, TimeoutException) as err:
            logging.error(f"Exception Type: {type(err)}")
            logging.info(f"Element does not exist: {(locator, )} ")
            return False
        return True

    def wait_for_clickable(self, locator, timeout=3):
        """ Check the element if it is clickable """
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable(locator)
            )
        except (NoSuchElementException, TimeoutException) as err:
            logging.error(f"Exception Type: {type(err)}")
            logging.info(f"Element does not exist: {(locator,)} ")
            return False
        return True

    def wait_for_invisible(self, locator, timeout=3):
        """ Check the element if it is invisible """
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.invisibility_of_element_located(locator)
            )
        except (NoSuchElementException, TimeoutException):
            return False
        return True

    def wait_for_text_present(self, locator, text, timeout=3):
        """ Check the text if the text is present """
        return WebDriverWait(self.driver, timeout).until(
            ec.text_to_be_present_in_element(locator, text))

    def wait_for_page_load(self):
        """
        Let pages inherit this function and overwrite it
        """
        pass

    def get_any_elements_by(self, by, timeout=3):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_any_elements_located(by)
            )
        except (NoSuchElementException, TimeoutException) as err:
            # logging.error(f"Exception Type: {type(err)}")
            # logging.error(f"No such element: {(by,)}")
            return None
        return element
