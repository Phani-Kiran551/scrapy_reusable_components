import scrapy, logging
from scrapy.loader import ItemLoader
from basics.items import BasicsItem
from scrapy.utils.project import get_project_settings


"""configurations"""

settings = get_project_settings()
FILES_URLS_LIST = settings.get("FILES_URLS_LIST")


class FileDownloader(scrapy.Spider):

    name = "file_downloader"

    start_urls = FILES_URLS_LIST

    """parse() gives us all the scraped files in this case mp3 files from the table present in the website."""

    def parse(self, response):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        for link in response.xpath(
            "//following::tr[4]/td[2]/a[not(contains(@href, 'jpg'))]"
        ):
            loader = ItemLoader(item=BasicsItem(), selector=link)
            relative_url = link.xpath(".//@href").extract_first()
            absolute_url = response.urljoin(relative_url)
            loader.add_value("file_urls", absolute_url)
            yield loader.load_item()
        logger.info(
            "returns all the scraped files in this case mp3 files from the table present in the website."
        )
