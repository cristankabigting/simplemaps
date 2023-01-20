import scrapy
import re

class IccspiderSpider(scrapy.Spider):

    name = 'iccspider'

    allowed_domains = ['philatlas.com']

    url = 'https://philatlas.com/'

    ext = '.html'

    start_urls = [
    
        url + 'mindanao/r12/cotabato-city' + ext,
        url + 'luzon/r01/pangasinan/dagupan' + ext,
        url + 'luzon/r05/camarines-sur/naga' + ext,
        url + 'visayas/r08/leyte/ormoc' + ext,
        url + 'luzon/r02/isabela/santiago' + ext
    ]

    def parse(self, response):
        locationname = response.xpath('//*[@id="mainHeadWrap"]/h1/text()').get()
        geotype = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[1]/td/a/text()').get()
        islandgroup = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[2]/td/a/text()').get()
        regionname = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[3]/td/a/text()').get()

        if locationname == 'Cotabato City':
            provincename = '';
            barangayCount = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[4]/td/text()').get()
            postalcode = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[5]/td/text()').get()
            coastal = response.xpath('//*[@id="borderType"]/text()').get()
            marine = response.xpath('//*[@id="adjMarine"]/text()').get()
            majorisland = islandgroup
            area = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[9]/td/text()').get()
            population = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[10]/td/text()').get()
            density = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[11]/td/text()').get()
            coordinates = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[12]/td/text()').get()
            elevation = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[13]/td/text()').get()
        else:
            provincename = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[4]/td/a/text()').get()
            barangayCount = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[5]/td/text()').get()
            postalcode = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[6]/td/text()').get()
            coastal = response.xpath('//*[@id="borderType"]/text()').get()
            marine = response.xpath('//*[@id="adjMarine"]/text()').get()
            majorisland = islandgroup
            area = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[10]/td/text()').get()
            population = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[11]/td/text()').get()
            density = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[12]/td/text()').get()
            coordinates = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[13]/td/text()').get()
            elevation = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[14]/td/text()').get()

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
            'provincename': provincename,
            'barangayCount': barangayCount,
            'postalcode': postalcode,
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