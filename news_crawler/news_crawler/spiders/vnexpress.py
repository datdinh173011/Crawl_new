import json
import scrapy
from datetime import datetime
import time

OUTPUT_FILENAME = 'Sohadata.txt'


class VnExpressSpider(scrapy.Spider):
    name = 'soha'
    allowed_domains = ['soha.vn']
    start_urls = ['https://soha.vn/trai-do-6-mui-ke-tuong-tan-cu-nga-chi-mang-cua-hot-girl-trung-ran-dinh-be-nhung-so-vuong-tam-nhin-nen-toi-vac-luon-20201226153858139.htm', ]
    crawled_count = 0

    def parse(self, response):
           print('Crawling from:', response.url)

           data = {
               'title': response.css('h1.news-title::text').get().strip(),
               'category': response.css('div[class = "clearfix mgt15 submenupagedetail"] a::text').getall()[0].strip(),
               # 'description': response.css('h2.news-sapo > a > ::text').get().strip(),
               'content': ''.join(
                   [''.join(c.css('*::text').getall()) for c in response.css('p')]).strip(),
           }
           with open(OUTPUT_FILENAME, 'a', encoding='utf8') as f:
               f.write(json.dumps(data, ensure_ascii=False))
               f.write('\n')
               self.crawled_count += 1
               self.crawler.stats.set_value('crawled_count', self.crawled_count)
               print('SUCCESS:', response.url)
           yield from response.follow_all(css='ul[class="related-news"] > li > a::attr(href)',
                                      callback=self.parse)



