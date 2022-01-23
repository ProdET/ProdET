import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tutorial.items import ProductItem

carouselPath = '//ol[@class="a-carousel" and @role="list"]'
carouselItemPath = carouselPath + \
    '//li[@class="a-carousel-card" and not(@aria-hidden="true")]'
carouselLinkPath = carouselItemPath + '//a[@class="a-link-normal"][2]'
carouselItemNamePath = carouselLinkPath + '//span//div'
carouselPricePath = carouselItemPath + \
    '//span[@class="a-size-base a-color-price"]//span'


gridPath = '//div[contains(@class,"desktop-grid")]'
gridItemPath = gridPath + '//div[@id="gridItemRoot"]'
gridLinkPath = gridItemPath + '//a[@class="a-link-normal"][2]'
gridItemNamePath = gridLinkPath + '//span//div'
gridPricePath = gridItemPath + \
    '//span[@class="a-size-base a-color-price"]//span'


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.ca', 'amazon.com']
    start_urls = [
        'https://www.amazon.ca/gp/bestsellers/',
    ]

    def parse(self, response):
        item = ProductItem()
        title = response.xpath('//h1[@id="title"]/span/text()').extract()
        sale_price = response.xpath(
            '//span[contains(@class,"a-price aok-align-center priceToPay")]//text()').extract()
        category = response.xpath(
            '//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
        if(category.contains('Back to results')):
            category = response.xpath(
                '//span[@class="cat-name"]/text()').extract()
        availability = response.xpath(
            '//div[@id="availability"]//text()').extract()
        item['product_name'] = ''.join(title).strip()
        item['product_sale_price'] = ''.join(sale_price).strip()
        item['product_category'] = ','.join(
            map(lambda x: x.strip(), category)).strip()
        item['product_availability'] = ''.join(availability).strip()
        item['product_link'] = response.request.url
        yield item

    """ #def parse(self, response):
        items = ProductItem()
        
        if(len(response.xpath(gridPath))>0):
            for item in response.xpath(gridPath):
                yield {
                    'itemName': item.xpath(gridItemNamePath).get(),
                    'price': item.xpath(gridPricePath).get(),
                    'link': item.xpath(gridLinkPath).attr('href'),
                }
        else:
            for item in response.xpath(carouselItemPath):
                    'itemName': item.xpath(carouselItemNamePath).get(),
                    'price': item.xpath(carouselPricePath).get(),
                    'link': item.xpath(carouselLinkPath).attr('href'),
                
            
        yield items """


class AmazonCarouselSpider(scrapy.Spider):
    name = 'amazonCarousel'
    allowed_domains = ['amazon.ca', 'amazon.com']
    start_urls = [
        'https://www.amazon.ca/',
        'https://www.amazon.com/',
        'https://www.amazon.ca/gp/bestsellers/',
    ]

    def parse(self, response):
        for item in response.xpath(carouselItemPath):
            yield {
                'itemName': item.xpath(carouselItemNamePath).get(),
                'price': item.xpath(carouselPricePath).get(),
                'link': item.xpath(carouselLinkPath).attr('href'),
            }
