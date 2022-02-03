import imp
from jmespath import search
import scrapy, logging
from scrapy.shell import inspect_response
from scrapy.utils.project import get_project_settings

"""configurations"""

settings = get_project_settings()
COOKIES_URLS_LIST = settings.get("COOKIES_URLS_LIST")


class DrsSpider(scrapy.Spider):

    name = "cookies_spider"

    start_urls = COOKIES_URLS_LIST
    custom_settings = {"COOKIES_ENABLED": True, "COOKIES_DEBUG": True}
    """parse() starts a scrapy interactive shell by which when we type in the above commands will get us the cookies."""

    def parse(self, response):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        inspect_response(response, self)
        """Go to the terminal and run
        
        ```bash
        spider using scrapy crawl drs
        ```
        and paste this command in the interactive shell.
        
        ```bash
        request.headers.get('Cookie').split(b';')[-1].decode().strip().replace(" ","")
        ```
        """

        logger.info(
            "starts a scrapy interactive shell by which when we type in the above commands will get us the cookies."
        )
