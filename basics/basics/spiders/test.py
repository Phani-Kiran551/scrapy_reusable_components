import configparser


parser = configparser.ConfigParser()
parser.read_file(open(r'/Users/buddaphanikiran/Desktop/scrapy_reusable_components/basics/basics/spiders/config.txt'))
print(parser.get("config", "TABLE_URLS_LIST"))
