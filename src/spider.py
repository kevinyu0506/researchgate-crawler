from scrapy import Request
from requests_html import HTML
from util.helper import get_reference, parse

import requests
import scrapy
import json
import os
import path as path


class PaperSpider(scrapy.Spider):
    name = 'paperspider'
    #start_urls = ['https://www.researchgate.net/publication/338506484_Less_Is_More_Learning_Highlight_Detection_From_Video_Duration']
    start_urls = ['https://www.researchgate.net/publication/323165042_Attention-based_Deep_Multiple_Instance_Learning']

    custom_settings = {
        'LOG_LEVEL': 'INFO',
        'DEPTH_LIMIT': 1,
        'DOWNLOAD_DELAY': 2.5,
    }

    def parse(self, response):
        follow_urls = set()

        url = response.url
        publication_id = url[url.find("publication")+12:url.find("_")]
        self.logger.info(f"current publication id: {publication_id}")

        title = response.xpath(path.TITLE).get() if not None else ""
        doi = response.xpath(path.DOI).get() if not None else ""
        conference = response.xpath(path.CONFERENCE).get() if not None else ""
        citation_count = response.xpath(path.CITATIONS_COUNT).get() if not None else ""
        citation_count = citation_count[citation_count.find("(")+1:citation_count.find(")")]
        reference_count = response.xpath(path.REFERENCES_COUNT).get() if not None else ""
        reference_count = reference_count[reference_count.find("(")+1:reference_count.find(")")]

        file_name = title.replace(" ","_")
        target_file = open(f'../output/{file_name}.json', 'w')

        paper_info = {
           'title': title,
           'DOI': doi,
           'conference': conference,
           'citation count': citation_count,
           'reference count': reference_count
        }

        target_file.write('{"result": ['+json.dumps(paper_info, indent=4)+',\n')

        target_file.close()

        offset = 10

        while get_reference(uid=publication_id, offset=offset).status_code == 200:
            ref_response = get_reference(uid=publication_id, offset=offset)
            #self.logger.info(ref_response.status_code)
            if (ref_response.text == ''):
                break
            html = HTML(html=ref_response.text)
            links = html.xpath(path.REFERENCES_LINK)
            if len(links) == 0:
                break
            for link in links:
                #self.logger.info(path.BASE_URL+link)
                follow_urls.add(path.BASE_URL+link)
            offset = offset + 5

        for reference in response.xpath(path.REFERENCES):
            reference_title = reference.xpath(path.REFERENCES_TITLE).get() if reference.xpath(path.REFERENCES_TITLE).get() is not None else ""
            reference_link = path.BASE_URL+reference.xpath(path.REFERENCES_LINK).get() if reference.xpath(path.REFERENCES_LINK).get() is not None else ""
            reference_type = reference.xpath(path.REFERENCES_TYPE).get() if reference.xpath(path.REFERENCES_TYPE).get() is not None else ""
            reference_date = reference.xpath(path.REFERENCES_DATE).get() if reference.xpath(path.REFERENCES_DATE).get() is not None else ""

            #self.logger.info(reference_link)
            if (reference_link != ''):
                follow_urls.add(reference_link)

        self.logger.info(f"total urls to follow: {len(follow_urls)}")

        for url in follow_urls:
            if url is not None:
                yield response.follow(url, self.reference_parse, cb_kwargs=dict(file_name=file_name))

    def reference_parse(self, response, file_name):
        reference_title = response.xpath(path.TITLE).get() if not None else ""
        reference_conference = response.xpath(path.CONFERENCE).get() if not None else ""
        reference_doi = response.xpath(path.DOI).get() if not None else ""
        reference_citation_count = response.xpath(path.CITATIONS_COUNT).get() if not None else ""
        reference_citation_count = reference_citation_count[reference_citation_count.find("(")+1:reference_citation_count.find(")")]

        target_file = open(f'../output/{file_name}.json', 'a')

        ref_info = {
            'reference title': reference_title,
            'ROI': reference_doi,
            'conference': reference_conference,
            'citation count': reference_citation_count,
        }

        target_file.write(json.dumps(ref_info, indent=4)+',\n')

        target_file.close()

    def closed(self, reason):
        with open(f'../output/Attention-based_Deep_Multiple_Instance_Learning.json', 'rb+') as target_file:
            target_file.seek(-1, os.SEEK_END)
            target_file.truncate()
            target_file.seek(-1, os.SEEK_END)
            target_file.truncate()

            target_file.close()


        target_file = open(f'../output/Attention-based_Deep_Multiple_Instance_Learning.json', 'a')

        target_file.write(']}')
        target_file.close()

        data = parse('../output/Attention-based_Deep_Multiple_Instance_Learning.json')
        self.logger.info(f'final scrap data length: {data}')
