import logging
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from job_post_scraper.spiders.job_finder import JobFinderSpider
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    crawler = CrawlerProcess(get_project_settings())
    crawler.crawl(JobFinderSpider)
    crawler.start()

