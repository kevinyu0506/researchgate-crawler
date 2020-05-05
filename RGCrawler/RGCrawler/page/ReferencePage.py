from selenium.webdriver.common.by import By
from RGCrawler.page.Page import Page

from time import sleep

import logging


class ReferencePage(Page):
    TITLE = (By.XPATH, "//h1")
    LOAD_MORE_BTN = (By.XPATH, "//span[contains(text(), 'Show more')]/..")
    CONFERENCE = (By.XPATH, "//div[contains(text(), 'Conference:')]")
    CONFERENCE_TYPE2 = (By.XPATH, "//a[contains(text(), 'Conference:')]")

    CITATION_BTN = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'Citations')]")
    CITATION_COUNT = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'Citations')]/strong")
    CITATION_COUNT_TYPE2 = (By.XPATH, "//div[@class='nova-c-nav__items']/a[1]//text()")

    REFERENCE_BTN = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'References')]")
    REFERENCE_COUNT = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'References')]/strong")
    REFERENCE_COUNT_TYPE2 = (By.XPATH, "//div[@class='nova-c-nav__items']/a[2]//text()")

    def __init__(self):
        super(ReferencePage).__init__()

    def perform(self):
        logging.info("-----Start interaction.-----")

        title = self.get_title()
        conference = self.get_conference()
        citation_count = self.get_citation_count()
        reference_count = self.get_reference_count()

        self.tap_reference_btn()
        self.load_all_references(citation_count, reference_count)

        logging.info("-----Interaction complete.-----")

        logging.info(f"root reference title: {title}")
        logging.info(f"root conference: {conference}")
        logging.info(f"root Citation: {citation_count}, root Reference: {reference_count}")

    def sub_perform(self):
        logging.info("-----Start sub interaction.-----")

        title = self.get_title()
        conference = self.get_conference()
        citation_count = self.get_citation_count()
        reference_count = self.get_reference_count()

        logging.info("-----Sub interaction complete.-----")

        logging.info(f"sub reference title: {title}")
        logging.info(f"sub conference: {conference}")
        logging.info(f"sub Citation: {citation_count}, sub Reference: {reference_count}")

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
            logging.info("Get title")
            return title.text
        else:
            logging.info("No title")
            return "TITLE NOT FOUND"

    def get_conference(self):
        conference = self.get_element_by(self.CONFERENCE)
        if conference is not None:
            logging.info("Get conference")
            n = conference.text
            # logging.info(f"String: {n}")
            n = n.split('Conference: ')[1]
            # logging.info(f"String2: {n}")
            return n
        else:
            conference2 = self.get_element_by(self.CONFERENCE_TYPE2)
            if conference2 is not None:
                logging.info("Get Conference type 2")
                n2 = conference2.text
                # logging.info(f"String: {n2}")
                n2 = n2.split('Conference: ')[1]
                # logging.info(f"String2: {n2}")
                return n2
            else:
                logging.info("No Conference")
                return None

    def get_citation_count(self):
        count = self.get_element_by(self.CITATION_COUNT)
        if count is not None:
            logging.info("Get citation count")
            n = count.text
            n = n.replace(',', '')
            return int(n)
        else:
            count2 = self.get_element_by(self.CITATION_COUNT_TYPE2)
            if count2 is not None:
                logging.info("Get citation count type 2")
                n2 = count2.text
                # logging.info(f"String: {n2}")
                n2 = n2[n2.find("(")+1:n2.find(")")]
                # logging.info(f"String2: {n2}")
                n2 = n2.replace(',', '')
                # logging.info(f"String3: {n2}")
                return int(n2)
            else:
                logging.info("No citation")
                return 0

    def get_reference_count(self):
        count = self.get_element_by(self.REFERENCE_COUNT)
        if count is not None:
            logging.info("Get reference count")
            n = count.text
            n = n.replace(',', '')
            return int(n)
        else:
            count2 = self.get_element_by(self.REFERENCE_COUNT_TYPE2)
            if count2 is not None:
                logging.info("Get reference count type 2")
                n2 = count2.text
                # logging.info(f"String: {n2}")
                n2 = n2[n2.find("(")+1:n2.find(")")]
                # logging.info(f"String2: {n2}")
                n2 = n2.replace(',', '')
                # logging.info(f"String3: {n2}")
                return int(n2)
            else:
                logging.info("No reference")
                return 0
