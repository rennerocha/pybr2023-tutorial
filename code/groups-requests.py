import requests
from parsel import Selector


start_urls = [
    "http://python.org.br",
]
for url in start_urls:
    response = requests.get(url)
    content = Selector(text=response.text)

    for group in content.css("h4.card-title::text").getall():
        print(group)
