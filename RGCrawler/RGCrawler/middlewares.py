# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.response import response_status_message
from scrapy.http import TextResponse
from scrapy.http import HtmlResponse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

import time


class RgcrawlerSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RgcrawlerDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TooManyRequestsRetryMiddleware(RetryMiddleware):

    def __init__(self, crawler):
        super(TooManyRequestsRetryMiddleware, self).__init__(crawler.settings)
        self.crawler = crawler

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            return response
        elif response.status == 429:
            self.crawler.engine.pause()
            time.sleep(5) # If the rate limit is renewed in a minute, put 60 seconds, and so on.
            self.crawler.engine.unpause()
            reason = response_status_message(response.status)
            return self._retry(request, reason, spider) or response
        elif response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            return self._retry(request, reason, spider) or response
        return response


# class CustomProxyMiddleware(object):
#
#     def process_request(self, request, spider):
#         request.headers["Proxy-Authorization"] = basic_auth_header("<proxy_user>", "<proxy_pass>")
#         request.meta["proxy"] = "http://192.168.1.1:8050"


class SeleniumChrome(object):

    def process_request(self, request, spider):
        if request.meta['driver'] == 'chrome':
            driver = spider.driver
            driver.get(request.url)
            body = driver.page_source
            return TextResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        return None

class SeleniumMiddleware():
    # Middleware中会传递进来一个spider，这就是我们的spider对象，从中可以获取__init__时的chrome相关元素
    LOAD_MORE_BTN = (By.XPATH,"//button[@class='nova-c-button nova-c-button--align-center nova-c-button--radius-m nova-c-button--size-xs nova-c-button--color-grey nova-c-button--theme-ghost nova-c-button--width-auto js-lite-click']")
    REF_BTN = (By.XPATH, "//button[contains(@class,'nova-c-nav__item references')]")

    def process_request(self, request, spider):
        '''
        用chrome抓取页面
        :param request: Request请求对象
        :param spider: Spider对象
        :return: HtmlResponse响应
        '''
        print(f"chrome is getting page")
        # 依靠meta中的标记，来决定是否需要使用selenium来爬取
        usedSelenium = request.meta.get('usedSelenium', False)
        if usedSelenium:
            try:
                spider.driver.get(request.url)
                time.sleep(15)

                self.scroll_to_element(spider.driver, self.REF_BTN)
                ref_btn = self.get_element_by(spider.driver, self.REF_BTN, 10)
                ref_btn.click()
                print(f"ref btn clicked")
                time.sleep(3)
                self.scroll_to_element(spider.driver, self.LOAD_MORE_BTN)
                print(f"Scroll to load more btn")

                while self.get_element_by(spider.driver, self.LOAD_MORE_BTN, 10) is not None:
                    self.wait_for_clickable(spider.driver, self.LOAD_MORE_BTN)
                    load_more_btn = self.get_element_by(spider.driver, self.LOAD_MORE_BTN)
                    load_more_btn.click()
                    print(f"load more btn clicked")
                    time.sleep(1)
                print(f"perform action done")

            except Exception as e:
                print(f"chrome getting page error, Exception = {e}")
                return HtmlResponse(url=request.url, status=500, request=request)
            else:
                print(f"return html response")
                time.sleep(3)
                # 页面爬取成功，构造一个成功的Response对象(HtmlResponse是它的子类)
                return HtmlResponse(url=request.url,
                                    body=spider.driver.page_source,
                                    request=request,
                                    # 最好根据网页的具体编码而定
                                    encoding='utf-8',
                                    status=200)

    def get_element_by(self, driver, by, timeout=5):
        try:
            element = WebDriverWait(driver, timeout).until(
                ec.visibility_of_element_located(by)
            )
        except (NoSuchElementException, TimeoutException) as err:
            print(f"Exception Type: {type(err)}")
            print(f"No such element: {(by,)}")
            return None
        return element

    def scroll_to_element(self, driver, by):
        element = self.get_element_by(driver, by)

        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

    def wait_for_clickable(self, driver, locator, timeout=10):
        """ Check the element if it is clickable """
        try:
            WebDriverWait(driver, timeout).until(
                ec.element_to_be_clickable(locator)
            )
        except (NoSuchElementException, TimeoutException) as err:
            return False
        return True
