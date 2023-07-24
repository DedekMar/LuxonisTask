import scrapy
from pathlib import Path
import json

import scrapy
from scraper.items import EstateItem


class QuotesSpider(scrapy.Spider):
    name = "sreality_scraper"

    def start_requests(self):
        # get all 500 results directly from seznams api
        urls = [
            "https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)

        for estate in data["_embedded"]["estates"]:
            estate_title = f"{estate['name']} {estate['locality']}"
            imgURLarr = estate["_links"]["image_middle2"]
            imgURL = imgURLarr[0]["href"]
            estate_item = EstateItem(title = estate_title, imgURL = imgURL)

            yield estate_item

