import scrapy, os
'''import io'''
'''import PyPDF2'''

class EIA_860M_Spider(scrapy.Spider):

    name = "EIA_860M"

    def start_requests(self):
    
        urls = ['https://www.eia.gov/electricity/data/eia860m/',]
        
        for url in urls:
        
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
    
        for link in response.xpath('//div[@class="pagecontent mpub_temp"]//table[@class="simpletable"]//thead//tr//td/a/@href').extract():
        
            absoluteLink = response.urljoin(link)
            
            yield scrapy.Request(url = absoluteLink, callback = self.parse_links)
            
            '''break'''


    def parse_links(self, response):
    
        page = response.url.split("/")[-1]
        
        filename = 'EIA-860M_%s' % page
        
        with open('/Users/andrewjackson/Personal Projects/VirtualEnvelope/scrapy_env_3.6/tutorial' + '/' + filename, 'wb') as f:
        
            f.write(response.body)
            
        self.log('Saved file %s' % filename)
