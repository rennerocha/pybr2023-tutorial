import scrapy


class PythonGroupsSpider(scrapy.Spider):
    name = "pythongroups"

    start_urls = [
        "http://python.org.br",
    ]

    def parse(self, response):
        groups = response.css('.card')
        for group in groups:
            yield {
                "name": group.css('h4::text').get(),
                "links": group.css('a::attr(href)').getall(),
            }
