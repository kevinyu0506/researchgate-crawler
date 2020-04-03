import scrapy

from RGCrawler.items import ReferenceItem
from RGCrawler.items import PaperItem

from scrapy.selector import Selector

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class RGSpider(scrapy.Spider):
    name = "RGSpider"
    download_delay = 10

    # Locators
    REFERENCES = "//div[contains(@class, 'js-target-references')]//li[@class='nova-e-list__item publication-citations__item']//div[@class='nova-v-publication-item__body']"
    REFERENCE_TITLE = ".//div[contains(@class,'nova-v-publication-item__title')]/a/text()"
    REFERENCE_DATE = ".//div[@class='nova-v-publication-item__meta-right']/ul/li[@class='nova-e-list__item nova-v-publication-item__meta-data-item']/span/text()"
    REFERENCE_CONFERENCE = ".//div[@class='nova-v-publication-item__meta-right']/ul//a[@class='nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare']/text()"
    TITLE = "//h1/text()"
    SITE_URL = "https://www.researchgate.net/publication/322584236_Towards_the_Understanding_of_Gaming_Audiences_by_Modeling_Twitch_Emotes"
    LOAD_MORE_REQUEST = "https://www.researchgate.net/lite.PublicationDetailsLoadMore.getReferencesByOffset.html?publicationUid=322584236&offset=10"
    LOAD_MORE_BTN = (By.XPATH, "//button[@class='nova-c-button nova-c-button--align-center nova-c-button--radius-m nova-c-button--size-xs nova-c-button--color-grey nova-c-button--theme-ghost nova-c-button--width-auto js-lite-click']")
    LOAD_MORE_BTN_XPATH = "//button[@class='nova-c-button nova-c-button--align-center nova-c-button--radius-m nova-c-button--size-xs nova-c-button--color-grey nova-c-button--theme-ghost nova-c-button--width-auto js-lite-click']"
    REF_BTN = (By.XPATH, "//button[contains(@class,'nova-c-nav__item references')]")
    REF_BTN_XPATH = "//button[contains(@class,'nova-c-nav__item references')]"

    start_urls = [SITE_URL]

    def __init__(self):
        super(RGSpider, self).__init__()
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get(self.SITE_URL)
        sleep(3)
        self.scroll_to_element(self.driver, self.REF_BTN)
        sleep(3)
        ref_btn = self.get_element_by(self.driver, self.REF_BTN, 10)
        ref_btn.click()
        sleep(3)
        self.scroll_to_element(self.driver, self.LOAD_MORE_BTN)
        while self.get_element_by(self.driver, self.LOAD_MORE_BTN, 10) is not None:
            load_more_btn = self.get_element_by(self.driver, self.LOAD_MORE_BTN)
            load_more_btn.click()
            sleep(3)

        response = Selector(text=self.driver.page_source)

        p_item = PaperItem()
        p_item['root_title'] = response.xpath(self.TITLE).get()
        yield p_item

        references = response.xpath(self.REFERENCES)

        for index, reference in enumerate(references):
            rf_item = ReferenceItem()
            rf_item['id'] = index
            rf_item['date'] = reference.xpath(self.REFERENCE_DATE).get()
            rf_item['title'] = reference.xpath(self.REFERENCE_TITLE).get()
            rf_item['conference'] = reference.xpath(self.REFERENCE_CONFERENCE).get()
            yield rf_item

        self.driver.quit()

    def get_element_by(self, driver, by, timeout=5):
        try:
            element = WebDriverWait(driver, timeout).until(
                ec.visibility_of_element_located(by)
            )
        except (NoSuchElementException, TimeoutException) as err:
            self.logger.error(f"Exception Type: {type(err)}")
            self.logger.error(f"No such element: {(by, )}")
            return None
        return element

    def scroll_to_element(self, driver, by):
        element = self.get_element_by(self.driver, by)

        actions = ActionChains(driver)
        actions.move_to_element(element).perform()