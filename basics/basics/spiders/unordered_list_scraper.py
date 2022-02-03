import scrapy, logging
from csv import writer
import csv
from scrapy.utils.project import get_project_settings

"""configurations"""

settings = get_project_settings()
UNORDERED_URLS_LIST = settings.get("UNORDERED_URLS_LIST")


class MyprojectSpider(scrapy.Spider):
    name = "project"
    start_urls = UNORDERED_URLS_LIST

    """parse() to scrape all the unordered lists from the website."""

    def parse(self, response):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        for sel in response.xpath("//ul/li"):
            try:
                title = sel.xpath("a/text()").extract()
                if title == "" or title == " " or title == "  ":
                    pass
                else:
                    yield {"title": sel.xpath("a/text()").extract()}
                    try:
                        with open("event.csv", "a") as f_object:

                            writer_object = writer(f_object)

                            writer_object.writerow(list(title))

                            f_object.close()
                    except:
                        print("Cannot open the file.")

            except:
                pass
        logger.info("Returns all the scraped unordered lists from the website.")
