import scrapy

from RGCrawler.items import ReferenceItem
from RGCrawler.items import PaperItem

from scrapy import Request

from RGCrawler.page.ReferencePage import ReferencePage

from RGCrawler.ranker import Ranker


class RGSpider(scrapy.Spider):
    name = "RGSpider"
    custom_settings = {
        # 'CONCURRENT_REQUESTS': 1,
        'LOG_LEVEL': 'INFO',
        # 'DOWNLOAD_DELAY': 3,
        'COOKIES_ENABLED': False,  # enabled by default
        'DOWNLOADER_MIDDLEWARES': {
            # 'RGCrawler.middlewares.ProxiesMiddleware': 400,
            'RGCrawler.middlewares.SeleniumMiddleware': 543,
            # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        }
    }

    # XPaths
    TITLE = "//h1/text()"
    CITATION_COUNT = "//div[@class='nova-o-pack__item']//div[contains(text(),'Citations')]/strong/text()"
    CITATION_COUNT_TYPE_2 = "//div[@class='nova-c-nav__items']/a[1]//text()"
    REFERENCE_COUNT = "//div[@class='nova-o-pack__item']//div[contains(text(),'References')]/strong/text()"
    REFERENCE_COUNT_TYPE2 = "//div[@class='nova-c-nav__items']/a[2]//text()"
    REFERENCES = "//div[@class='nova-v-citation-item']"
    # REFERENCES = "//div[contains(@class, 'js-target-references')]//li[@class='nova-e-list__item publication-citations__item']//div[@class='nova-v-publication-item__body']"
    REFERENCE_TITLE_LINKABLE = ".//div[@class='nova-v-publication-item__stack-item']/div/a/text()"
    # REFERENCE_TITLE_LINKABLE = ".//div[contains(@class,'nova-v-publication-item__title')]/a/text()"
    REFERENCE_LINK = ".//div[@class='nova-v-publication-item__stack-item']/div/a/@href"
    # REFERENCE_LINK = ".//div[contains(@class,'nova-v-publication-item__title')]/a/@href"
    REFERENCE_TITLE_UNLINKABLE = ".//div[contains(@class,'nova-v-publication-item__title')]/text()"
    REFERENCE_DATE = ".//div[@class='nova-v-publication-item__meta-right']/ul/li[@class='nova-e-list__item nova-v-publication-item__meta-data-item']/span/text()"
    REFERENCE_CONFERENCE = ".//div[@class='nova-v-publication-item__meta-right']/ul//a[@class='nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare']/text()"

    CONFERENCE = "//div[contains(text(), 'Conference:')]/text()"
    CONFERENCE_TYPE2 = "//a[contains(text(), 'Conference:')]/text()"

    def __init__(self, endpoint=None):
        self.heap = Ranker()
        self.url = "https://www.researchgate.net/publication/" + endpoint
        super(RGSpider, self).__init__()

    def start_requests(self):
        yield Request(
            url=self.url,
            meta={'usedSelenium': True, 'dont_redirect': True, 'root': True},
            callback=self.parse_reference
        )

    @staticmethod
    def start_interaction(driver):
        ReferencePage().set_driver(driver).perform()

    @staticmethod
    def start_sub_interaction(driver):
        ReferencePage().set_driver(driver).sub_perform()

    def parse_sub_reference(self, response):
        rf_item = ReferenceItem()
        rf_item['title'] = response.request.meta.get('title', 'title META NULL')
        rf_item['link'] = response.request.url

        try:
            c_count = response.xpath(self.CITATION_COUNT).get()
            c_count = c_count.replace(',', '')
            rf_item['citation_count'] = int(c_count)
        except Exception as e:
            rf_item['citation_count'] = 0

        if rf_item['citation_count'] == 0:
            try:
                c_count = response.xpath(self.CITATION_COUNT_TYPE_2).get()
                c_count = c_count[c_count.find("(")+1:c_count.find(")")]
                c_count = c_count.replace(',', '')
                rf_item['citation_count'] = int(c_count)
            except Exception as e:
                rf_item['citation_count'] = 0

        try:
            r_count = response.xpath(self.REFERENCE_COUNT).get()
            r_count = r_count.replace(',', '')
            rf_item['reference_count'] = int(r_count)
        except Exception as e:
            rf_item['reference_count'] = 0

        if rf_item['reference_count'] == 0:
            try:
                r_count = response.xpath(self.REFERENCE_COUNT_TYPE2).get()
                r_count = r_count[r_count.find("(")+1:r_count.find(")")]
                r_count = r_count.replace(',', '')
                rf_item['reference_count'] = int(r_count)
            except Exception as e:
                rf_item['reference_count'] = 0

        rf_item['date'] = response.request.meta.get('date', 'date META NULL')

        try:
            conf = response.xpath(self.CONFERENCE).get()
            conf = conf.split('Conference: ')[1]
            rf_item['conference'] = conf
        except Exception as e:
            rf_item['conference'] = None

        if rf_item['conference'] is None:
            try:
                conf2 = response.xpath(self.CONFERENCE_TYPE2).get()
                conf2 = conf2.split('Conference: ')[1]
                rf_item['conference'] = conf2
            except Exception as e:
                rf_item['conference'] = None

        yield rf_item

    def parse_reference(self, response):
        self.logger.info("===============Start root parsing")

        p_item = PaperItem()
        p_item['target_title'] = response.xpath(self.TITLE).get()
        p_item['target_link'] = self.url

        try:
            c_count = response.xpath(self.CITATION_COUNT).get()
            c_count = c_count.replace(',', '')
            p_item['target_citation_count'] = int(c_count)
        except Exception as e:
            p_item['target_citation_count'] = 0

        try:
            r_count = response.xpath(self.REFERENCE_COUNT).get()
            r_count = r_count.replace(',', '')
            p_item['target_reference_count'] = int(r_count)
        except Exception as e:
            p_item['target_reference_count'] = 0

        yield p_item

        references = response.xpath(self.REFERENCES)
        for reference in references:
            if reference.xpath(self.REFERENCE_TITLE_LINKABLE).get() is not None:
                link = "https://www.researchgate.net/" + reference.xpath(self.REFERENCE_LINK).get()

                title = reference.xpath(self.REFERENCE_TITLE_LINKABLE).get()
                date = reference.xpath(self.REFERENCE_DATE).get()
                conference = reference.xpath(self.REFERENCE_CONFERENCE).get()

                yield Request(
                    url=link,
                    meta={'usedSelenium': True,
                          'dont_redirect': True,
                          'root': False,
                          'title': title,
                          'date': date,
                          'conference': conference},
                    callback=self.parse_sub_reference
                )

            elif reference.xpath(self.REFERENCE_TITLE_UNLINKABLE).get():
                rf_item = ReferenceItem()
                rf_item['title'] = reference.xpath(self.REFERENCE_TITLE_UNLINKABLE).get()
                rf_item['link'] = None
                rf_item['citation_count'] = 0
                rf_item['reference_count'] = 0
                rf_item['date'] = reference.xpath(self.REFERENCE_DATE).get()
                rf_item['conference'] = reference.xpath(self.REFERENCE_CONFERENCE).get()
                yield rf_item

        self.logger.info("===============Parse root complete.")
