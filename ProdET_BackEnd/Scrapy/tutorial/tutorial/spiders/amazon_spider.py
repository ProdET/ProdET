import scrapy

carouselPath = '//ol[@class="a-carousel" and @role="list"]'
carouselItemPath = carouselPath + '//li[@class="a-carousel-card" and not(@aria-hidden="true")]'
carouselLinkPath = carouselItemPath + '//a[@class="a-link-normal"][2]'
carouselItemNamePath = carouselLinkPath + '//span//div'
carouselPricePath = carouselItemPath + '//span[@class="a-size-base a-color-price"]//span'
    
class AmazonCarouselSpider(scrapy.Spider):
    name = 'amazonCarousel'
    allowed_domains = ['amazon.ca','amazon.com']
    start_urls = [
        'https://www.amazon.ca/',
        'https://www.amazon.com/',
    ]
    
    def parse(self, response):
        for item in response.xpath(carouselItemPath):
            yield {
                'itemName': item.xpath(carouselItemNamePath).get(),
                'price': item.xpath(carouselPricePath).get(),
                'link': item.xpath(carouselLinkPath).attr('href'),
            }

gridPath = '//div[contains(@class,"desktop-grid")]'
gridItemPath = gridPath + '//div[@id="gridItemRoot"]'
gridLinkPath = gridItemPath + '//a[@class="a-link-normal"][2]'
gridItemNamePath = gridLinkPath + '//span//div'
gridPricePath = gridItemPath + '//span[@class="a-size-base a-color-price"]//span'
class AmazonGridSpider(scrapy.Spider):
    name = 'amazonGrid'
    allowed_domains = ['amazon.ca','amazon.com']
    start_urls = [
        'https://www.amazon.ca/gp/bestsellers/',
    ]
    def parse(self, response):
        for item in response.xpath(gridPath):
            yield {
                'itemName': item.xpath(gridItemNamePath).get(),
                'price': item.xpath(gridPricePath).get(),
                'link': item.xpath(gridLinkPath).attr('href'),
            }