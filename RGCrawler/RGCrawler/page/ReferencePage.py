from selenium.common.exceptions import NoSuchElementException, TimeoutException

from selenium.webdriver.common.by import By
from RGCrawler.page.Page import Page

from time import sleep

import logging


class ReferencePage(Page):
    # Locators
    TITLE = (By.XPATH, "//h1")
    LOAD_MORE_BTN = (By.XPATH, "//span[contains(text(), 'Show more')]/..")
    REF_BTN = (By.XPATH, "//button[contains(@class,'nova-c-nav__item references')]")

    CITATION_BTN = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'Citations')]")
    CITATION_COUNT = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'Citations')]/strong")
    CITATION_COUNT_TYPE2 = (By.XPATH, "//div[@class='nova-c-nav__items']/a[1]//text()")
    REFERENCE_BTN = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'References')]")
    REFERENCE_COUNT = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'References')]/strong")
    REFERENCE_COUNT_TYPE2 = (By.XPATH, "//div[@class='nova-c-nav__items']/a[2]//text()")

    def __init__(self):
        super(ReferencePage).__init__()

    def perform(self):
        logging.info("Start interaction.")

        title = self.get_title()
        citation_count = self.get_citation_count()
        reference_count = self.get_reference_count()

        logging.info(f"root reference title: {title}")
        logging.info(f"root Citation: {citation_count}, root Reference: {reference_count}")
        self.tap_reference_btn()
        self.load_all_references(citation_count, reference_count)

        logging.info("Interaction complete.")

    def sub_perform(self):
        logging.info("Start sub interaction.")

        title = self.get_title()
        citation_count = self.get_citation_count()
        reference_count = self.get_reference_count()

        logging.info(f"sub reference title: {title}")
        logging.info(f"sub Citation: {citation_count}, sub Reference: {reference_count}")

        logging.info("Sub interaction complete.")

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

    def get_title(self):
        title = self.get_element_by(self.TITLE)
        if title is not None:
            return title.text
        else:
            return "TITLE NOT FOUND"

    def get_citation_count(self):
        count = self.get_element_by(self.CITATION_COUNT)

        if count is not None:
            n = count.text
            n = n.replace(',', '')
            return int(n)
        else:
            logging.info("ReferencePage c_count switch mode.")
            count2 = self.get_element_by(self.CITATION_COUNT_TYPE2)
            if count2 is not None:
                n2 = count2.text
                logging.info(f"String: {n2}")
                n2 = n2[n2.find("(")+1:n2.find(")")]
                logging.info(f"String2: {n2}")
                n2 = n2.replace(',', '')
                logging.info(f"String3: {n2}")
                return int(n2)
            else:
                return 0

    def get_reference_count(self):
        count = self.get_element_by(self.REFERENCE_COUNT)
        if count is not None:
            n = count.text
            n = n.replace(',', '')
            return int(n)
        else:
            logging.info("ReferencePage r_count switch mode.")
            count2 = self.get_element_by(self.REFERENCE_COUNT_TYPE2)
            if count2 is not None:
                n2 = count2.text
                logging.info(f"String: {n2}")
                n2 = n2[n2.find("(")+1:n2.find(")")]
                logging.info(f"String2: {n2}")
                n2 = n2.replace(',', '')
                logging.info(f"String3: {n2}")
                return int(n2)
            else:
                return 0