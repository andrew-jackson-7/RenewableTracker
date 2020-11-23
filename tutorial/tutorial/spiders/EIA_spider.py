import scrapy, os
import io
import PyPDF2


class QuotesSpider(scrapy.Spider):
    name = "EIA"

    def start_requests(self):
        urls = ['https://www.eia.gov/electricity/monthly/',]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    '''def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.txt' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)'''

    def parse(self, response):
        for link in response.xpath('//div[@class="report_header"]//span[@class="left rtitle"]//p/a/@href').extract():
            absoluteLink = response.urljoin(link)
            
            ''' Adding line of code to print out URL --- 5/17/2020'''
            
            self.log(absoluteLink)
            
            '''End of what was added on 5/17/2020'''
            
            yield scrapy.Request(url = absoluteLink, callback = self.parse_pdf)


    '''def parse_links(self, response):
        page = response.url.split("/")[-2]
        filename = 'EIA-%s.txt' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)'''

    def parse_pdf(self, response):
        read_PDF = PyPDF2.PdfFileReader(io.BytesIO(response.body))
        page_PDF = read_PDF.getPage(163)

        '''Adding code to generate a PDF --- 3/16/2020; Andrew.'''

        file_name = 'EIA_Extracted_Page'

        output_PDF = PyPDF2.PdfFileWriter()
        output_PDF.addPage(page_PDF)

        with open('/Users/andrewjackson/Personal Projects/VirtualEnvelope/scrapy_env_3.6/tutorial' + '/' + file_name + '.pdf', "wb") as out_file:
            output_PDF.write(out_file)

        '''End of what Andrew added on 3/16/2020.'''
        
        page_content = page_PDF.extractText()
        page = response.url.split("/")[-2]
        '''self.log(page_content)'''
        page_content_segment = page_content.partition("Table 6.5. Planned U.S. Electric Generating Unit Additions")[2]
        self.log(page_content_segment.splitlines()[1])

'''import scrapy, os

class legco(scrapy.Spider):
    name = "sec_gov"

    start_urls = ["https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&SIC=2834&owner=exclude&match=&start=120&count=40&hidefilings=0"]

    def parse(self, response):
        for link in response.xpath('//table[@summary="Results"]//td[@scope="row"]/a/@href').extract():
            absoluteLink = response.urljoin(link)
            yield scrapy.Request(url = absoluteLink, callback = self.parse_links)

        nextpage = response.css("input[value='Next 40']::attr(onclick)")
        if nextpage:
            tpage = nextpage.extract_first().split("parent.location=")[1].replace("'","")
            nlink = response.urljoin(tpage)
            yield scrapy.Request(url=nlink, callback = self.parse)

    def parse_links(self, response):
        for links in response.xpath('//table[@summary="Results"]//a[@id="documentsbutton"]/@href').extract():
            targetLink = response.urljoin(links)
            yield scrapy.Request(url = targetLink, callback = self.collecting_file_links)

    def collecting_file_links(self, response):
        for links in response.xpath('//table[contains(@summary,"Document")]//tr[td[starts-with(., "EX-")]]/td/a[contains(@href, ".htm") or contains(@href, ".txt")]/@href').extract():
            baseLink = response.urljoin(links)
            yield scrapy.Request(url = baseLink, callback = self.download_files)

    def download_files(self, response):
        path = response.url.split('/')[-1]
        dirf = r"/home/surukam/scrapy/demo/tutorial/tutorial/Downloads3"
        if not os.path.exists(dirf):os.makedirs(dirf)
        os.chdir(dirf)
        with open(path, 'wb') as f:
            f.write(response.body)'''
