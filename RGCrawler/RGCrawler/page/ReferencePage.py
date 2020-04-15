from selenium.common.exceptions import NoSuchElementException, TimeoutException

from selenium.webdriver.common.by import By
from RGCrawler.page.Page import Page

from time import sleep

import logging


class ReferencePage(Page):
    # Locators
    LOAD_MORE_BTN = (By.XPATH, "//span[contains(text(), 'Show more')]/..")
    REF_BTN = (By.XPATH, "//button[contains(@class,'nova-c-nav__item references')]")

    CITATION_BTN = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'Citations')]")
    CITATION_COUNT = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'Citations')]/strong")
    REFERENCE_BTN = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'References')]")
    REFERENCE_COUNT = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'References')]/strong")

    def __init__(self):
        super(ReferencePage).__init__()

    def perform(self):
        logging.info("Start interaction.")

        citation_count = self.get_citation_count()
        reference_count = self.get_reference_count()
        logging.info(f"Citation: {citation_count}, Reference: {reference_count}")
        self.tap_reference_btn()
        self.load_all_references(citation_count, reference_count)

        logging.info("Interaction complete.")

    def tap_reference_btn(self):
        ref_btn = self.get_element_by(self.REFERENCE_BTN)
        ref_btn.click()

        logging.info("Ref btn clicked.")

    def load_all_references(self, citation_count, reference_count):
        while self.get_any_elements_by(self.LOAD_MORE_BTN, 10) is not None:
            if citation_count < 10 and reference_count > 10:
                self.driver.execute_script("document.getElementsByClassName('nova-c-button nova-c-button--align-center nova-c-button--radius-m nova-c-button--size-xs nova-c-button--color-grey nova-c-button--theme-ghost nova-c-button--width-auto js-lite-click')[0].click();")
            elif citation_count > 10 and reference_count > 10:
                self.driver.execute_script("document.getElementsByClassName('nova-c-button nova-c-button--align-center nova-c-button--radius-m nova-c-button--size-xs nova-c-button--color-grey nova-c-button--theme-ghost nova-c-button--width-auto js-lite-click')[1].click();")
            logging.info("Load more btn clicked.")
            sleep(1)

        logging.info("Load all references complete.")
        sleep(3)

    def get_citation_count(self):
        count = self.get_element_by(self.CITATION_COUNT)
        if count is not None:
            return int(count.text)
        else:
            return 0

    def get_reference_count(self):
        count = self.get_element_by(self.REFERENCE_COUNT)
        if count is not None:
            return int(count.text)
        else:
            return 0
