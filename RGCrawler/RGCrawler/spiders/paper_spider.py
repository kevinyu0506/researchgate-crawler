import scrapy

from RGCrawler.items import ReferenceItem
from RGCrawler.items import PaperItem


# //div[contains(@class, 'js-target-references')]//li[@class='nova-e-list__item publication-citations__item']//div[@class='nova-v-publication-item__body']"
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


class PaperSpider(scrapy.Spider):
    name = "papers"

    download_delay = 10
    start_urls = [SITE_URL]

    def parse(self, response):
        p_item = PaperItem()
        p_item['root_title'] = response.xpath(TITLE).get()
        yield p_item

        references = response.xpath(REFERENCES)

        for index, reference in enumerate(references):
            rf_item = ReferenceItem()
            rf_item['id'] = index
            rf_item['date'] = reference.xpath(REFERENCE_DATE).get()
            rf_item['title'] = reference.xpath(REFERENCE_TITLE).get()
            rf_item['conference'] = reference.xpath(REFERENCE_CONFERENCE).get()
            yield rf_item
