import logging
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from job_post_scraper.spiders.job_post_scraper import JobFinderSpider
import email_jobs


if __name__ == '__main__':
    # So DB has a log of success & errors
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # Main execution of crawler (removes need to use scrapy <command> <project>
    crawler = CrawlerProcess(get_project_settings())
    crawler.crawl(JobFinderSpider)
    crawler.start()
    email_jobs

