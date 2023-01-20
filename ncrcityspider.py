import scrapy
import re

class NcrcityspiderSpider(scrapy.Spider):
    
    name = 'ncrcityspider'

    allowed_domains = ['philatlas.com']

    url = 'https://philatlas.com/luzon/ncr/'

    ext = '.html'

    start_urls = [
    
        url + 'caloocan' + ext,
        url + 'las-pinas' + ext,
        url + 'makati' + ext,
        url + 'malabon' + ext,
        url + 'mandaluyong' + ext,
        url + 'manila' + ext,
        url + 'marikina' + ext,
        url + 'muntinlupa' + ext,
        url + 'navotas' + ext,
        url + 'paranaque' + ext,
        url + 'pasay' + ext,
        url + 'pasig' + ext,
        url + 'pateros' + ext,
        url + 'quezon-city' + ext,
        url + 'san-juan' + ext,
        url + 'taguig' + ext,
        url + 'valenzuela' + ext

    ]

    def parse(self, response):

        locationname = response.xpath('//*[@id="mainHeadWrap"]/h1/text()').get()
        geotype = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[1]/td/a/text()').get()
        islandgroup = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[2]/td/a/text()').get()
        regionname = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[3]/td/a/text()').get()
        barangayCount = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[4]/td/text()').get()
        coastal = response.xpath('//*[@id="borderType"]/text()').get()
        marine = response.xpath('//*[@id="adjMarine"]/text()').get()
        majorisland = islandgroup
        area = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[8]/td/text()').get()
        population = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[9]/td/text()').get()
        density = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[10]/td/text()').get()
        coordinates = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[11]/td/text()').get()
        elevation = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[12]/td/text()').get()
        latitude = response.xpath('//*[@id="latitude"]/text()').get()
        longitude = response.xpath('//*[@id="longitude"]/text()').get()

        nlgu = ''
        for p in response.css('#nearestLgusNote'):
            nlgu += " ".join(p.xpath('.//text()').extract())
            nlgu = re.sub(r'<.*?>', '', nlgu)
            nlgu = " ".join(nlgu.split())

        nplace = ''
        for p in response.css('#sectionDistancesDet'):
            nplace += " ".join(p.xpath('.//text()').extract())
            nplace = re.sub(r'<.*?>', '', nplace)
            nplace = " ".join(nplace.split())

        distmanila = ''

        for p in response.css('#fromManila'):
            distmanila += " ".join(p.xpath('.//text()').extract())
            distmanila = re.sub(r'<.*?>', '', distmanila)
            distmanila = " ".join(distmanila.split())

        articles = '';
        
        for p in response.css('.articleContent'):
            articles += " ".join(p.xpath('.//text()').extract())
            articles = re.sub(r'<.*?>', '', articles)
            articles = articles.replace('(adsbygoogle = window.adsbygoogle || []).push({});', '')
            articles = articles.replace('‑', ' to ')
            articles = articles.replace('Maps utilize OpenStreetMap data available under the Open Data Commons Open Database License.(Back to top)', '')
            articles = " ".join(articles.split())

        yield {
            'locationname': locationname,
            'geotype': geotype,
            'islandgroup': islandgroup,
            'regionname': regionname.replace(u' ',u' '),
            'barangayCount': barangayCount,
            'coastal': coastal,
            'marine': marine.replace(u' ',u' '),
            'majorisland': majorisland,
            'area':area,
            'population': population,
            'density': density,
            'coordinates': coordinates.replace(u' ',u' '),
            'elevation': elevation.replace(u' ',u' '),
            'latitude': latitude,
            'longitude':longitude,
            'nlgu':nlgu,
            'nplace': nplace.replace(u' ',u' '),
            'distmanila':distmanila.replace(u' ',u' '),
            'articles': articles.replace(u' ',u' ')
        }