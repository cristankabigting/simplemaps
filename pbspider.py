import scrapy
import re

class PbspiderSpider(scrapy.Spider):
    
    name = 'pbspider'

    allowed_domains = ['philatlas.com']

    custom_settings = {
        'FEEDS': { 'zzz.json': { 'format': 'json', 'encoding': 'utf8','overwrite': True } }
    }

    def start_requests(self):

        # read file data (you can use different logic for extract URLS from text files)

        a_file = open("C:/Users/Admin/Desktop/Scrapy/LinkSpider/links.txt")

        file_contents = a_file.read()

        contents_split = file_contents.splitlines()

        # extract urls from text file and store in list

        for url in contents_split:
            # send request to extracted URL.
            yield scrapy.Request(url)    

    # start_urls = [

    # ]

    def parse(self, response):
        
        inputtype = 'huc'

        bodycontent = ''

        locationname = response.xpath('//*[@id="mainHeadWrap"]/h1/text()').get()

        adjacentbrgy = response.xpath('//*[@id="adjacent-bgy-list"]//text()').extract()

        articles = '';
        
        for p in response.css('.articleContent'):
            articles += " ".join(p.xpath('.//text()').extract())
            articles = re.sub(r'<.*?>', '', articles)
            articles = articles.replace('(adsbygoogle = window.adsbygoogle || []).push({});', '')
            articles = articles.replace('‑', ' to ')
            articles = articles.replace('Maps utilize OpenStreetMap data available under the Open Data Commons Open Database License.(Back to top)', '')
            articles = " ".join(articles.split())

        for p in response.xpath("//div[@id='iboxWrap']/table[@class='iBox']"):
            geotype = "".join(p.xpath('.//tr[1]/td/a/text()').extract())
            islandgroup = "".join(p.xpath('.//tr[2]/td/a/text()').extract())
            regionname = "".join(p.xpath('.//tr[3]/td/a/text()').extract())

            if (inputtype == 'common'):
                cityname = ''
                provincename = "".join(p.xpath('.//tr[4]/td/a/text()').extract())
                municipalityname = "".join(p.xpath('.//tr[5]/td/a/text()').extract())
                postalcode = "".join(p.xpath('.//tr[6]/td/text()').extract())
                population = "".join(p.xpath('.//tr[7]/td/text()').extract())
                majorisland = "".join(p.xpath('.//tr[8]/td/a/text()').extract())
                coordinates = "".join(p.xpath('.//tr[9]/td/span[2]/following-sibling::text()').extract()).replace(' , (','(').replace('(','').replace(')','').strip()
                elevation = "".join(p.xpath('.//tr[10]/td/text()').extract())
                latitude = "".join(p.xpath('.//tr[9]/td/span[1]/text()').extract())
                longitude = "".join(p.xpath('.//tr[9]/td/span[2]/text()').extract())

            if (inputtype == 'ncr'):
                provincename = ''
                municipalityname = ''
                postalcode = ''
                cityname = "".join(p.xpath('.//tr[4]/td/a/text()').extract())
                population = "".join(p.xpath('.//tr[5]/td/text()').extract())
                majorisland = "".join(p.xpath('.//tr[6]/td/a/text()').extract())
                coordinates = "".join(p.xpath('.//tr[7]/td/span[2]/following-sibling::text()').extract()).replace(' , (','(').replace('(','').replace(')','').strip()
                elevation = "".join(p.xpath('.//tr[8]/td/text()').extract())
                latitude = "".join(p.xpath('.//tr[7]/td/span[1]/text()').extract())
                longitude = "".join(p.xpath('.//tr[7]/td/span[2]/text()').extract())

            if (inputtype == 'huc'):
                provincename = ''
                municipalityname = ''
                cityname = "".join(p.xpath('.//tr[4]/td/a/text()').extract())
                postalcode = "".join(p.xpath('.//tr[5]/td/text()').extract())
                population = "".join(p.xpath('.//tr[6]/td/text()').extract())
                majorisland = "".join(p.xpath('.//tr[7]/td/a/text()').extract())
                coordinates = "".join(p.xpath('.//tr[8]/td/span[2]/following-sibling::text()').extract()).replace(' , (','(').replace('(','').replace(')','').strip()
                elevation = "".join(p.xpath('.//tr[9]/td/text()').extract())
                latitude = "".join(p.xpath('.//tr[8]/td/span[1]/text()').extract())
                longitude = "".join(p.xpath('.//tr[8]/td/span[2]/text()').extract())

        yield {
            'locationname': locationname.replace(u' ',u' '),
            'geotype': geotype,
            'islandgroup':islandgroup,
            'regionname': regionname.replace(u' ',u' '),
            'provincename':provincename,
            'cityname': cityname.replace(u' ',u' '),
            'municipalityname':municipalityname,
            'postalcode':postalcode,
            'population':population,
            'majorisland':majorisland,
            'coordinates':coordinates.replace(u' ',u' '),
            'elevation': elevation.replace(u' ',u' '),
            'latitude':latitude,
            'longitude':longitude,
            'articles': articles,
            'adjacentbrgy':adjacentbrgy
        }