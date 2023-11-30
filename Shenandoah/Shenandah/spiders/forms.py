import scrapy


class FormsSpider(scrapy.Spider):
    name = "forms"
    allowed_domains = ["shenandoahcountyva.us"]
    start_urls = ["https://shenandoahcountyva.us/revenue/forms/"]

    def parse(self, response):
        headers = response.xpath('//div[@class="entry-content"]/ul/li')
        for header in headers :
            question = header.xpath('//div[@class="entry-content"]/ul/li/h3/text()')
            answer = header.xpath('//div[@class="entry-content"]/ul/li/p/text()')

            yield {
                'Question' : question,
                'Answer' : answer
            }

        
