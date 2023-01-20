import scrapy
import re

class RegionspiderSpider(scrapy.Spider):
    
    name = 'regionspider'
    
    allowed_domains = ['philatlas.com']

    start_urls = [
        'https://philatlas.com/luzon/r01.html',
        'https://philatlas.com/luzon/r02.html',
        'https://philatlas.com/luzon/r03.html',
        'https://philatlas.com/luzon/r04a.html',
        'https://philatlas.com/luzon/r05.html',
        'https://philatlas.com/luzon/mimaropa.html',
        'https://philatlas.com/visayas/r06.html',
        'https://philatlas.com/visayas/r07.html',
        'https://philatlas.com/visayas/r08.html',
        'https://philatlas.com/mindanao/r09.html',
        'https://philatlas.com/mindanao/r10.html',
        'https://philatlas.com/mindanao/r11.html',
        'https://philatlas.com/mindanao/r12.html',
        'https://philatlas.com/mindanao/caraga.html',
        'https://philatlas.com/luzon/ncr.html',
        'https://philatlas.com/luzon/car.html',
        'https://philatlas.com/mindanao/barmm.html',
    ]

    def parse(self, response):

        locationname = response.xpath('//*[@id="mainHeadWrap"]/h1/text()').get()
        geotype = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[2]/td/a/text()').get()
        islandgroup = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[3]/td/a/text()').get()
        provinceCount = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[4]/td/text()').get()
        cityCount = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[5]/td/text()').get()
        municipalityCount = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[6]/td/text()').get()
        barangayCount = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[7]/td/text()').get()
        coastal = response.xpath('//*[@id="borderType"]/text()').get()
        marine = response.xpath('//*[@id="adjMarine"]/text()').get()
        area = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[10]/td/text()').get()
        population = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[11]/td/text()').get()
        density = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[12]/td/text()').get()

        articles = '';
        
        for p in response.css('.articleContent'):
            articles += "".join(p.xpath('.//text()').extract())
            articles = re.sub(r'<.*?>', '', articles)
            articles = articles.replace('(adsbygoogle = window.adsbygoogle || []).push({});', '')
            articles = articles.replace('‑', ' to ')
            articles = articles.replace('Maps utilize OpenStreetMap data available under the Open Data Commons Open Database License.(Back to top)', '')
            articles = " ".join(articles.split())

        yield {
            'locationname': locationname,
            'geotype': geotype,
            'islandgroup': islandgroup,
            'provinceCount': provinceCount,
            'cityCount': cityCount,
            'municipalityCount': municipalityCount,
            'barangayCount': barangayCount,
            'coastal': coastal,
            'marine': marine.replace(u' ',u' '),
            'area':area,
            'population': population,
            'density': density,
            'articles': articles.replace(u' ',u' ')
        }