import scrapy

from RGCrawler.items import ReferenceItem
from RGCrawler.items import PaperItem

from scrapy import Request

from time import sleep

from RGCrawler.page import ReferencePage

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class RGSpider(scrapy.Spider):
    name = "RGSpider"
    download_delay = 10
    custom_settings = {
        'LOG_LEVEL': 'INFO',
        'DOWNLOAD_DELAY': 0,
        'COOKIES_ENABLED': False,  # enabled by default
        'DOWNLOADER_MIDDLEWARES': {
            # 'RGCrawler.middlewares.ProxiesMiddleware': 400,
            'RGCrawler.middlewares.SeleniumMiddleware': 543,
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        }
    }

    # Locators
    REFERENCES = "//div[contains(@class, 'js-target-references')]//li[@class='nova-e-list__item publication-citations__item']//div[@class='nova-v-publication-item__body']"
    REFERENCE_TITLE_LINKABLE = ".//div[contains(@class,'nova-v-publication-item__title')]/a/text()"
    REFERENCE_LINK = ".//div[contains(@class,'nova-v-publication-item__title')]/a/@href"
    REFERENCE_TITLE_UNLINKABLE = ".//div[contains(@class,'nova-v-publication-item__title')]/text()"
    REFERENCE_DATE = ".//div[@class='nova-v-publication-item__meta-right']/ul/li[@class='nova-e-list__item nova-v-publication-item__meta-data-item']/span/text()"
    REFERENCE_CONFERENCE = ".//div[@class='nova-v-publication-item__meta-right']/ul//a[@class='nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare']/text()"
    TITLE = "//h1/text()"
    # SITE_URL = "https://www.researchgate.net/publication/322584236_Towards_the_Understanding_of_Gaming_Audiences_by_Modeling_Twitch_Emotes"
    # SITE_URL = "https://www.researchgate.net/publication/314361240_Spice_up_Your_Chat_The_Intentions_and_Sentiment_Effects_of_Using_Emoji"
    SITE_URL = "https://www.researchgate.net/publication/313910429_Are_Emojis_Predictable"
    LOAD_MORE_BTN = (By.XPATH, "//span[contains(text(), 'Show more')]/..")
    REF_BTN = (By.XPATH, "//button[contains(@class,'nova-c-nav__item references')]")

    POPUP_BTN = (By.XPATH, "//button[@class='nova-c-button nova-c-button--align-center nova-c-button--radius-m nova-c-button--size-xs nova-c-button--color-grey nova-c-button--theme-bare nova-c-button--width-auto']")

    CITATION_BTN = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'Citations')]")
    CITATION_COUNT = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'Citations')]/strong")
    REFERENCE_BTN = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'References')]")
    REFERENCE_COUNT = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'References')]/strong")

    start_urls = [SITE_URL]

    # Nice Article: https://blog.csdn.net/zwq912318834/article/details/79773870
    #               https://github.com/Jamesway/scrapy-demo/blob/master/scrapy_dca/spiders/dca_spider.py
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        super(RGSpider, self).__init__()

    def start_requests(self):
        # since we need selenium to interact with js btn, we're going to override
        # the request generated automatically by the framework and create our own.
        #
        # We yield this request and pass it to our custom SeleniumMiddleware for further handling

        yield Request(
            url=self.SITE_URL,
            meta={'usedSelenium': True, 'dont_redirect': True},
            callback=self.parse_reference
        )

    def start_interaction(self):
        self.logger.info("Start interaction.")

        citation_count = self.get_citation_count()
        reference_count = self.get_reference_count()
        self.logger.info(f"Citation: {citation_count}, Reference: {reference_count}")

        ref_btn = self.get_element_locate_by(self.driver, self.REFERENCE_BTN)
        ref_btn.click()
        self.logger.info("Ref btn clicked.")

        while self.get_any_elements_by(self.driver, self.LOAD_MORE_BTN, 10) is not None:
            # self.logger.info("Load more tab fetched.")
            # load_more_btn = self.get_any_elements_by(self.driver, self.LOAD_MORE_BTN)
            # self.logger.info(f"len(): {len(load_more_btn)}")
            # load_more_btn[0].click()
            if citation_count < 10 and reference_count > 10:
                self.driver.execute_script("document.getElementsByClassName('nova-c-button nova-c-button--align-center nova-c-button--radius-m nova-c-button--size-xs nova-c-button--color-grey nova-c-button--theme-ghost nova-c-button--width-auto js-lite-click')[0].click();")
            elif citation_count > 10 and reference_count > 10:
                self.driver.execute_script("document.getElementsByClassName('nova-c-button nova-c-button--align-center nova-c-button--radius-m nova-c-button--size-xs nova-c-button--color-grey nova-c-button--theme-ghost nova-c-button--width-auto js-lite-click')[1].click();")
            self.logger.info("Load more btn clicked.")
            sleep(1)

        self.logger.info("Load all btn, interaction complete.")
        sleep(3)

    def get_citation_count(self):
        count = self.get_element_locate_by(self.driver, self.CITATION_COUNT).text
        self.logger.info(f"Citation string: {count}")
        return int(count)

    def get_reference_count(self):
        count = self.get_element_locate_by(self.driver, self.REFERENCE_COUNT).text
        self.logger.info(f"Reference string: {count}")
        return int(count)

    def parse_reference(self, response):
        self.logger.info("Start parsing")

        p_item = PaperItem()
        p_item['root_title'] = response.xpath(self.TITLE).get()
        yield p_item

        references = response.xpath(self.REFERENCES)
        for index, reference in enumerate(references):
            rf_item = ReferenceItem()
            rf_item['id'] = index
            if reference.xpath(self.REFERENCE_TITLE_LINKABLE).get() is not None:
                rf_item['title'] = reference.xpath(self.REFERENCE_TITLE_LINKABLE).get()
                rf_item['link'] = "https://www.researchgate.net/" + reference.xpath(self.REFERENCE_LINK).get()
            elif reference.xpath(self.REFERENCE_TITLE_UNLINKABLE).get():
                rf_item['title'] = reference.xpath(self.REFERENCE_TITLE_UNLINKABLE).get()
                rf_item['link'] = None
            rf_item['date'] = reference.xpath(self.REFERENCE_DATE).get()
            rf_item['conference'] = reference.xpath(self.REFERENCE_CONFERENCE).get()
            yield rf_item

        self.logger.info("Parse complete.")
        self.driver.quit()

    def get_element_locate_by(self, driver, by, timeout=5):
        try:
            element = WebDriverWait(driver, timeout).until(
                ec.visibility_of_element_located(by)
            )
        except (NoSuchElementException, TimeoutException) as err:
            self.logger.error(f"Exception Type: {type(err)}")
            self.logger.error(f"No such element: {(by, )}")
            return None
        return element

    def get_any_elements_by(self, driver, by, timeout=10):
        try:
            element = WebDriverWait(driver, timeout).until(
                ec.visibility_of_any_elements_located(by)
            )
        except (NoSuchElementException, TimeoutException) as err:
            self.logger.error(f"Exception Type: {type(err)}")
            self.logger.error(f"No such element: {(by,)}")
            return None
        return element
