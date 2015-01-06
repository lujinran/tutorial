import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---/m?kw=%E7%81%AB%E7%88%86%E5%A4%A9%E7%8E%8B&lp=7202",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)