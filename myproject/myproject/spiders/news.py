import scrapy

from myproject.items import Headline

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['https://news.yahoo.co.jp/']

    # 取得したWebページを処理するためのコールバック関数
    # def parse(self, response):
    #     print(response.css('#liveStream > div > h2').extract())

    def parse(self, response):
        print(response.css('ul.topicsList_main a::attr("href")').re(r'/pickup/\d+$'))
        for url in response.css('ul.topicsList_main a::attr("href")').re(r'/pickup/\d+$'):
            yield scrapy.Request(response.urljoin(url), self.parse_topics)

    def parse_topics(self, response):
        item = Headline()
        item['title'] = response.css('.pickupMain_articleTitle ::text').extract_first()
        item['body'] = response.css('.pickupMain_articleSummary ::text').extract_first()
        yield item
