BASE_URL = "https://www.researchgate.net/"

# request token
RG_REQUEST_TOKEN = "//meta[@name='Rg-Request-Token']"

# paper info
TITLE = "//h1/text()"
DATE = "//div[@class='research-detail-header-section__metadata']/div[1]//li/text()"
DOI = "//div[contains(text(),'DOI:')]/a/text()"
CONFERENCE = "//li[contains(text(),'Conference:')]/text()"
CITATIONS_COUNT = "//div[contains(text(),'Citations')]/text()"
REFERENCES_COUNT = "//div[contains(text(),'References')]/text()"


# references section
REFERENCES = "//div[@class='js-target-reference']//div[@class='nova-v-citation-item']"
# references title
REFERENCES_TITLE = ".//div[contains(@class,'nova-v-publication-item__title')]/a/text()"
# referecnes hyper link (might be null)
REFERENCES_LINK = ".//div[contains(@class,'nova-v-publication-item__title')]//@href"
# references type (eg. Article, Conference Paper, Null)
REFERENCES_TYPE = ".//span[contains(@class,'nova-v-publication-item__type')]/text()"
# references authors
REFERENCES_AUTHOR = ".//ul[contains(@class,'nova-v-publication-item__person-list')]/text()"
# references date
REFERENCES_DATE = ".//div[@class='nova-v-publication-item__meta-right']//span/text()"
