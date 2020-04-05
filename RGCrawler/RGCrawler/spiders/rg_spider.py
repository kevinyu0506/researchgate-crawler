import scrapy

from RGCrawler.items import ReferenceItem
from RGCrawler.items import PaperItem

from scrapy.http import TextResponse
from scrapy import Selector

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


class RGSpider(scrapy.Spider):
    name = "RGSpider"
    download_delay = 10

    # Locators
    REFERENCES = "//div[contains(@class, 'js-target-references')]//li[@class='nova-e-list__item publication-citations__item']//div[@class='nova-v-publication-item__body']"
    REFERENCE_TITLE_LINKABLE = ".//div[contains(@class,'nova-v-publication-item__title')]/a/text()"
    REFERENCE_LINK = ".//div[contains(@class,'nova-v-publication-item__title')]/a/@href"
    REFERENCE_TITLE_UNLINKABLE = ".//div[contains(@class,'nova-v-publication-item__title')]/text()"
    REFERENCE_DATE = ".//div[@class='nova-v-publication-item__meta-right']/ul/li[@class='nova-e-list__item nova-v-publication-item__meta-data-item']/span/text()"
    REFERENCE_CONFERENCE = ".//div[@class='nova-v-publication-item__meta-right']/ul//a[@class='nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare']/text()"
    TITLE = "//h1/text()"
    SITE_URL = "https://www.researchgate.net/publication/322584236_Towards_the_Understanding_of_Gaming_Audiences_by_Modeling_Twitch_Emotes"
    # SITE_URL = "https://www.researchgate.net/publication/314361240_Spice_up_Your_Chat_The_Intentions_and_Sentiment_Effects_of_Using_Emoji"
    LOAD_MORE_REQUEST = "https://www.researchgate.net/lite.PublicationDetailsLoadMore.getReferencesByOffset.html?publicationUid=322584236&offset=10"
    LOAD_MORE_BTN = (By.XPATH, "//button[@class='nova-c-button nova-c-button--align-center nova-c-button--radius-m nova-c-button--size-xs nova-c-button--color-grey nova-c-button--theme-ghost nova-c-button--width-auto js-lite-click']")
    LOAD_MORE_BTN_XPATH = "//button[@class='nova-c-button nova-c-button--align-center nova-c-button--radius-m nova-c-button--size-xs nova-c-button--color-grey nova-c-button--theme-ghost nova-c-button--width-auto js-lite-click']"
    REF_BTN = (By.XPATH, "//button[contains(@class,'nova-c-nav__item references')]")
    REF_BTN_XPATH = "//button[contains(@class,'nova-c-nav__item references')]"

    start_urls = [SITE_URL]

    def __init__(self):
        super(RGSpider, self).__init__()
        opts = Options()
        opts.add_argument('Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
        self.driver = webdriver.Chrome(chrome_options=opts)

        # response = self.get_selenium_response()
        # self.logger.info("Get selenium response succeed.")
        # # yield response.follow(self.SITE_URL, self.parse)
        # self.parse_reference(response)
        # self.logger.info("Parse to parser.")

    def start_requests(self):
        # overriding start_requests() is not usually necessary unless:
        # - we need to use selenium to interact with a form
        # - we want to customize parts of the request object
        #
        # if we don't override start_requests(),
        # scrapy generates requests from urls in start_urls[]
        # and calls parse() as the default callback
        #
        # for s in self.start_urls:
        #     request = self.make_requests_from_url(s)
        #     # request.callback = self.parse_shell
        #
        #     yield request
        #
        # since we need selenium for the js form interactions we're going to circumvent creating a request
        # instead we create a scrapy response object from the selenium form results
        # then we use the xpath selector of the response object to create links to follow

        response = self.get_selenium_response()
        self.logger.info("Get selenium response succeed.")
        yield response.follow(self.SITE_URL, self.parse)
        self.logger.info("Parse to parser.")

    def get_selenium_response(self):
        self.logger.info("Start to get selenium response")
        self.driver.get(self.SITE_URL)
        self.scroll_to_element(self.driver, self.REF_BTN)
        self.logger.info("Scroll to ref tab.")
        ref_btn = self.get_element_by(self.driver, self.REF_BTN, 10)
        ref_btn.click()
        self.logger.info("Ref tab clicked.")
        while self.get_element_by(self.driver, self.LOAD_MORE_BTN, 5) is not None:
            load_more_btn = self.get_element_by(self.driver, self.LOAD_MORE_BTN)
            load_more_btn.click()
            self.logger.info("Load more btn clicked.")
            # sleep(1)

        self.logger.info("Load all btn.")
        sleep(3)

        r = TextResponse(url=self.driver.current_url, body=self.driver.page_source, encoding='utf-8')
        # r = self.driver.page_source
        self.logger.info("Generate response")
        # self.parse_reference(response)
        return r

    def parse(self, response):
        response = scrapy.Selector(text=self.get_selenium_response())
        # response = response.meta.get('html')

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
            rf_item['date'] = reference.xpath(self.REFERENCE_DATE).get()
            rf_item['conference'] = reference.xpath(self.REFERENCE_CONFERENCE).get()
            yield rf_item

        self.logger.info("Parse selenium response succeed.")
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
