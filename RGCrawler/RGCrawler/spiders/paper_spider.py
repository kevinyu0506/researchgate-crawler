import scrapy

from RGCrawler.items import ReferenceItem
from RGCrawler.items import PaperItem

# from scrapy.spidermiddlewares.httperror import HttpError
# from twisted.internet.error import DNSLookupError
# from twisted.internet.error import TimeoutError, TCPTimedOutError


# //div[contains(@class, 'js-target-references')]//li[@class='nova-e-list__item publication-citations__item']//div[@class='nova-v-publication-item__body']
REFERENCES = "//div[contains(@class, 'js-target-references')]" \
             "//li[@class='nova-e-list__item publication-citations__item']" \
             "//div[@class='nova-v-publication-item__body']"

REFERENCE_TITLE = ".//div[contains(@class,'nova-v-publication-item__title')]/a/text()"

# .//div[@class='nova-v-publication-item__meta-right']/ul/li[@class='nova-e-list__item nova-v-publication-item__meta-data-item']/span/text()
REFERENCE_DATE = ".//div[@class='nova-v-publication-item__meta-right']/ul" \
                 "/li[@class='nova-e-list__item nova-v-publication-item__meta-data-item']/span/text()"

# .//div[@class='nova-v-publication-item__meta-right']/ul//a[@class='nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare']/text()
REFERENCE_CONFERENCE = ".//div[@class='nova-v-publication-item__meta-right']/ul" \
                       "//a[@class='nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare']/text()"

TITLE = "//h1/text()"

SITE_URL = "https://www.researchgate.net/publication/" \
           "322584236_Towards_the_Understanding_of_Gaming_Audiences_by_Modeling_Twitch_Emotes"

# https://www.researchgate.net/lite.PublicationDetailsLoadMore.getReferencesByOffset.html?publicationUid=322584236&offset=10
LOAD_MORE = "https://www.researchgate.net/" \
            "lite.PublicationDetailsLoadMore.getReferencesByOffset.html?publicationUid=322584236&offset=10"


class PaperSpider(scrapy.Spider):
    name = "papers"

    download_delay = 10
    start_urls = [SITE_URL]

    def parse(self, response):
        p_item = PaperItem()
        p_item['root_title'] = response.xpath(TITLE).get()
        self.logger.info(f"Root title: {p_item['root_title']}")
        yield p_item

        references = response.xpath(REFERENCES)

        for index, reference in enumerate(references):
            rf_item = ReferenceItem()
            rf_item['id'] = index
            rf_item['date'] = reference.xpath(REFERENCE_DATE).get()
            rf_item['title'] = reference.xpath(REFERENCE_TITLE).get()
            rf_item['conference'] = reference.xpath(REFERENCE_CONFERENCE).get()
            self.logger.info(f"ref{index} title: {rf_item['title']}, date: {rf_item['date']}")
            yield rf_item

        # scrapy.Request(LOAD_MORE,
        #                method='POST',
        #                callback=self.parse_load,
        #                errback=self.parse_load_fail)

    # def parse_load(self, response):
    #     references = response.xpath(REFERENCES)
    #
    #     for index, reference in enumerate(references):
    #         rf_item = ReferenceItem()
    #         rf_item['id'] = index
    #         rf_item['date'] = reference.xpath(REFERENCE_DATE).get()
    #         rf_item['title'] = reference.xpath(REFERENCE_TITLE).get()
    #         rf_item['conference'] = reference.xpath(REFERENCE_CONFERENCE).get()
    #         yield rf_item

    # def parse_load_fail(self, failure):
    #     # log all failures
    #     self.logger.error(repr(failure))
    #
    #     # in case you want to do something special for some errors,
    #     # you may need the failure's type:
    #
    #     if failure.check(HttpError):
    #         # these exceptions come from HttpError spider middleware
    #         # you can get the non-200 response
    #         response = failure.value.response
    #         self.logger.error(f'HttpError on {response.url}')
    #
    #     elif failure.check(DNSLookupError):
    #         # this is the original request
    #         request = failure.request
    #         self.logger.error(f'DNSLookupError on {request.url}')
    #
    #     elif failure.check(TimeoutError, TCPTimedOutError):
    #         request = failure.request
    #         self.logger.error(f'TimeoutError on {request.url}')
