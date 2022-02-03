import scrapy, logging, re
from scrapy.utils.project import get_project_settings

"""configurations"""

settings = get_project_settings()
IMAGE_URLS_LIST = settings.get("IMAGE_URLS_LIST")


class ImageSpider(scrapy.Spider):
    name = "paris"
    start_urls = IMAGE_URLS_LIST

    """parse() returns all the scraped images from the website."""

    def parse(self, response):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        raw_image_urls = response.css(".image img ::attr(src)").getall()
        clean_image_urls = []
        for img_url in raw_image_urls:
            clean_image_urls.append(response.urljoin(img_url))

        yield {"image_urls": clean_image_urls}
        logger.info("Returns all the scraped images from the website.")
