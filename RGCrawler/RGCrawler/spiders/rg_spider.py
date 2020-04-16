import scrapy

from RGCrawler.items import ReferenceItem
from RGCrawler.items import PaperItem

from scrapy import Request

from RGCrawler.page.ReferencePage import ReferencePage

from selenium import webdriver


# Nice Article: https://blog.csdn.net/zwq912318834/article/details/79773870
#               https://github.com/Jamesway/scrapy-demo/blob/master/scrapy_dca/spiders/dca_spider.py
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

    # XPaths
    TITLE = "//h1/text()"
    CITATION_COUNT = "//div[@class='nova-o-pack__item']//div[contains(text(),'Citations')]/strong/text()"
    REFERENCE_COUNT = "//div[@class='nova-o-pack__item']//div[contains(text(),'References')]/strong/text()"
    REFERENCES = "//div[contains(@class, 'js-target-references')]//li[@class='nova-e-list__item publication-citations__item']//div[@class='nova-v-publication-item__body']"
    REFERENCE_TITLE_LINKABLE = ".//div[contains(@class,'nova-v-publication-item__title')]/a/text()"
    REFERENCE_LINK = ".//div[contains(@class,'nova-v-publication-item__title')]/a/@href"
    REFERENCE_TITLE_UNLINKABLE = ".//div[contains(@class,'nova-v-publication-item__title')]/text()"
    REFERENCE_DATE = ".//div[@class='nova-v-publication-item__meta-right']/ul/li[@class='nova-e-list__item nova-v-publication-item__meta-data-item']/span/text()"
    REFERENCE_CONFERENCE = ".//div[@class='nova-v-publication-item__meta-right']/ul//a[@class='nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare']/text()"

    # Target site
    # SITE_URL = "https://www.researchgate.net/publication/322584236_Towards_the_Understanding_of_Gaming_Audiences_by_Modeling_Twitch_Emotes"
    # SITE_URL = "https://www.researchgate.net/publication/314361240_Spice_up_Your_Chat_The_Intentions_and_Sentiment_Effects_of_Using_Emoji"
    # SITE_URL = "https://www.researchgate.net/publication/313910429_Are_Emojis_Predictable"
    SITE_URL = "https://www.researchgate.net/publication/336551306_Unsupervised_Multi-stream_Highlight_detection_for_the_Game_Honor_of_Kings"

    start_urls = [SITE_URL]

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        super(RGSpider, self).__init__()

    def start_requests(self):
        # since we need selenium to interact with js btn, we're going to override
        # the request generated automatically by the framework and create our own.
        #
        # for s in self.start_urls:
        #         request = self.make_requests_from_url(s)
        #         request.callback = self.parse_shell
        #
        #         yield request
        #
        # We yield this request and pass it to our custom SeleniumMiddleware for further handling
        yield Request(
            url=self.SITE_URL,
            meta={'usedSelenium': True, 'dont_redirect': True, 'root': True},
            callback=self.parse_reference
        )

    def start_interaction(self):
        self.logger.info("Start perform.")
        ReferencePage().set_driver(self.driver).perform()
        self.logger.info("End perform.")

    def start_sub_interaction(self):
        self.logger.info("Start sub perform.")
        ReferencePage().set_driver(self.driver).sub_perform()
        self.logger.info("End sub perform.")

    def parse_sub_reference(self, response):
        self.logger.info("Start sub parsing")

        c_count = response.xpath(self.CITATION_COUNT).get()
        r_count = response.xpath(self.REFERENCE_COUNT).get()

        self.logger.info(f"Citation: {c_count}, Reference: {r_count}")
        # return [c_count, r_count]

    def parse_reference(self, response):
        self.logger.info("Start parsing")

        p_item = PaperItem()
        p_item['root_title'] = response.xpath(self.TITLE).get()
        p_item['root_link'] = self.SITE_URL
        p_item['citation_count'] = response.xpath(self.CITATION_COUNT).get()
        p_item['reference_count'] = response.xpath(self.REFERENCE_COUNT).get()

        reference_list = []

        references = response.xpath(self.REFERENCES)
        for index, reference in enumerate(references):
            rf_item = ReferenceItem()
            rf_item['id'] = index
            if reference.xpath(self.REFERENCE_TITLE_LINKABLE).get() is not None:
                rf_item['title'] = reference.xpath(self.REFERENCE_TITLE_LINKABLE).get()
                rf_item['link'] = "https://www.researchgate.net/" + reference.xpath(self.REFERENCE_LINK).get()

                yield Request(
                    url=rf_item['link'],
                    meta={'usedSelenium': True, 'dont_redirect': True, 'root': False},
                    callback=self.parse_sub_reference
                )
                rf_item['citation_count'] = response.xpath(self.CITATION_COUNT).get()
                rf_item['reference_count'] = response.xpath(self.REFERENCE_COUNT).get()

            elif reference.xpath(self.REFERENCE_TITLE_UNLINKABLE).get():
                rf_item['title'] = reference.xpath(self.REFERENCE_TITLE_UNLINKABLE).get()
                rf_item['link'] = None
                rf_item['citation_count'] = 0
                rf_item['reference_count'] = 0

            rf_item['date'] = reference.xpath(self.REFERENCE_DATE).get()
            rf_item['conference'] = reference.xpath(self.REFERENCE_CONFERENCE).get()
            # yield rf_item
            reference_list.append(rf_item)

        p_item['reference_list'] = reference_list
        yield p_item

        self.logger.info("Parse complete.")
        self.driver.quit()
