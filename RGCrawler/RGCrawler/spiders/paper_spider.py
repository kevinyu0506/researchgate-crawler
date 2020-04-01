import scrapy

from RGCrawler.items import RgcrawlerItem


REFERENCES = "//div[contains(@class, 'js-target-references')]" \
             "//li[@class='nova-e-list__item publication-citations__item']" \
             "//div[contains(@class,'nova-v-publication-item__title')]/a/text()"

SITE_URL = "https://www.researchgate.net/publication/" \
           "322584236_Towards_the_Understanding_of_Gaming_Audiences_by_Modeling_Twitch_Emotes"


class PaperSpider(scrapy.Spider):
    name = "papers"

    download_delay = 3
    start_urls = [SITE_URL]

    def parse(self, response):
        references = response.xpath(REFERENCES)

        for index, reference in enumerate(references):
            item = RgcrawlerItem()
            item['index'] = index
            item['title'] = reference.get()
            yield item
