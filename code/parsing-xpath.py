import scrapy


class PythonGroupsSpider(scrapy.Spider):
    name = "pythongroups"

    start_urls = [
        "http://python.org.br",
    ]

    def parse(self, response):
        groups = response.xpath('//div[contains(@class, "card")]')
        for group in groups:
            yield {
                "name": group.xpath('.//h4/text()').get(),
                "links": group.xpath('.//a/@href').getall(),
            }
