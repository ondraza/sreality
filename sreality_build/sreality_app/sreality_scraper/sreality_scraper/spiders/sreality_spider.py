import scrapy
import json

class SrealitySpider(scrapy.Spider):
        name = 'sreality'
        start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&sort=0&per_page=100&page='+str(x)+''for x in range(1, 6)]
        
        def parse(self, response):
            json_response = response.json()

            # debug
            with open('flats.json', 'w') as json_file:
                json.dump(json_response, json_file, indent=4)

            for flat in json_response['_embedded']['estates']:
                title = flat['name']
                img_url = flat['_links']['images'][0]['href']
                locality = flat['locality']
                price = str(flat['price'])
                yield {'title':title, 'img_url':img_url, 'locality':locality, 'price':price}