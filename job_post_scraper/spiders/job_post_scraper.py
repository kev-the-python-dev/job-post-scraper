from scrapy import Spider
from scrapy.selector import Selector

from job_post_scraper.items import YCombItem

'''The goal is to be able to crawl YCombinator.com, Reddit, and other various job post websites to identify jobs (including filters). 
We identify xpaths for specific fields (e.g. title, url, etc), extract to MongoDB, and eventually create a front-end people can 
access to have all job postings in a singular place.'''

# Specifically for YCombinator only
class JobFinderSpider(Spider):
    name = "job_post_scraper"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = [
            'https://news.ycombinator.com/jobs',
            ]

    def parse(self, response):
        # May 4th Update -> might be more convenient to use response.selector instead of constructing our own Selector object.
        # That way the response body is parsed only one time. Example --> questions = response.xpath('//tr[@class="athing"]')
        questions = Selector(response).xpath('//tr[@class="athing"]')

        for question in questions:
            item = YCombItem()
            # extrac() is an older Scrapy method but will update to get() as Scrapy docs claim it is more concise/readable when script scales in size
            item['title'] = question.xpath('td/a/text()').extract()[0]
            item['url'] = question.xpath('td/a[@class="titlelink"]/@href').extract()[0]
            yield item
