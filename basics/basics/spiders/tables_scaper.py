from logging.config import dictConfig
import requests, json, logging
from bs4 import BeautifulSoup
import configparser

parser = configparser.ConfigParser()
parser.read_file(
    open(
        r"/Users/buddaphanikiran/Desktop/scrapy_reusable_components/basics/basics/config.txt"
    )
)

TABLE_URLS_LIST = list(parser.get("config", "TABLE_URLS_LIST").split(","))


class WebScraping:
    """ init function to specify required variables."""

    def __init__(self, url):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        self.url = url
        logger.info("init function to specify required variables.")

    """web_scraping() returns all the scraped data from the selected columns in the table present in the website"""

    def web_scraping(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        dictionary = {}
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")
        league_table = soup.find("table", class_="standing-table__table callfn")
        for team in league_table.find_all("tbody"):
            rows = team.find_all("tr")
            for row in rows:
                p1_team = row.find(
                    "td", class_="standing-table__cell standing-table__cell--name"
                ).text.strip()
                p1_points = row.find_all("td", class_="standing-table__cell")[9].text
                print(p1_team, p1_points)
                dictionary.update({p1_team: p1_points})

        with open("output.json", "w") as outfile:
            json.dump(dictionary, outfile)

        logger.info(
            "returns all the scraped data from the selected columns in the table present in the website."
        )


def main():
    for url in TABLE_URLS_LIST:
        object = WebScraping(url)
        object.web_scraping()


if __name__ == "__main__":
    main()
