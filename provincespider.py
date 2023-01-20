import scrapy
import re

class ProvincespiderSpider(scrapy.Spider):

    name = 'provincespider'

    allowed_domains = ['philatlas.com']

    url = 'https://philatlas.com/'

    start_urls = [

        url + 'luzon/car/abra.html',
        url + 'mindanao/caraga/agusan-del-norte.html',
        url + 'mindanao/caraga/agusan-del-sur.html',
        url + 'visayas/r06/aklan.html',
        url + 'luzon/r05/albay.html',
        url + 'visayas/r06/antique.html',
        url + 'luzon/car/apayao.html',
        url + 'luzon/r03/aurora.html',
        url + 'mindanao/barmm/basilan.html',
        url + 'luzon/r03/bataan.html',
        url + 'luzon/r02/batanes.html',
        url + 'luzon/r04a/batangas.html',
        url + 'luzon/car/benguet.html',
        url + 'visayas/r08/biliran.html',
        url + 'visayas/r07/bohol.html',
        url + 'mindanao/r10/bukidnon.html',
        url + 'luzon/r03/bulacan.html',
        url + 'luzon/r02/cagayan.html',
        url + 'camarines-norte.html',
        url + 'luzon/r05/camarines-sur.html',
        url + 'mindanao/r10/camiguin.html',
        url + 'visayas/r06/capiz.html',
        url + 'luzon/r05/catanduanes.html',
        url + 'luzon/r04a/cavite.html',
        url + 'visayas/r07/cebu.html',
        url + 'mindanao/r12/cotabato.html',
        url + 'mindanao/r11/davao-de-oro.html',
        url + 'mindanao/r11/davao-del-norte.html',
        url + 'mindanao/r11/davao-del-sur.html',
        url + 'mindanao/r11/davao-occidental.html',
        url + 'mindanao/r11/davao-oriental.html',
        url + 'mindanao/caraga/dinagat-islands.html',
        url + 'visayas/r08/eastern-samar.html',
        url + 'visayas/r06/guimaras.html',
        url + 'luzon/car/ifugao.html',
        url + 'luzon/r01/ilocos-norte.html',
        url + 'luzon/r01/ilocos-sur.html',
        url + 'visayas/r06/iloilo.html',
        url + 'luzon/r02/isabela.html',
        url + 'luzon/car/kalinga.html',
        url + 'luzon/r01/la-union.html',
        url + 'luzon/r04a/laguna.html',
        url + 'mindanao/r10/lanao-del-norte.html',
        url + 'mindanao/barmm/lanao-del-sur.html',
        url + 'visayas/r08/leyte.html',
        url + 'mindanao/barmm/maguindanao.html',
        url + 'luzon/mimaropa/marinduque.html',
        url + 'luzon/r05/masbate.html',
        url + 'mindanao/r10/misamis-occidental.html',
        url + 'mindanao/r10/misamis-oriental.html',
        url + 'luzon/car/mountain-province.html',
        url + 'visayas/r06/negros-occidental.html',
        url + 'visayas/r07/negros-oriental.html',
        url + 'visayas/r08/northern-samar.html',
        url + 'luzon/r03/nueva-ecija.html',
        url + 'luzon/r02/nueva-vizcaya.html',
        url + 'luzon/mimaropa/occidental-mindoro.html',
        url + 'luzon/mimaropa/oriental-mindoro.html',
        url + 'luzon/mimaropa/palawan.html',
        url + 'luzon/r03/pampanga.html',
        url + 'luzon/r01/pangasinan.html',
        url + 'luzon/r04a/quezon.html',
        url + 'luzon/r02/quirino.html',
        url + 'luzon/r04a/rizal.html',
        url + 'luzon/mimaropa/romblon.html',
        url + 'visayas/r08/samar.html',
        url + 'mindanao/r12/sarangani.html',
        url + 'visayas/r07/siquijor.html',
        url + 'luzon/r05/sorsogon.html',
        url + 'mindanao/r12/south-cotabato.html',
        url + 'visayas/r08/southern-leyte.html',
        url + 'mindanao/r12/sultan-kudarat.html',
        url + 'mindanao/barmm/sulu.html',
        url + 'mindanao/caraga/surigao-del-norte.html',
        url + 'mindanao/caraga/surigao-del-sur.html',
        url + 'luzon/r03/tarlac.html',
        url + 'mindanao/barmm/tawi-tawi.html',
        url + 'luzon/r03/zambales.html',
        url + 'mindanao/r09/zamboanga-del-norte.html',
        url + 'mindanao/r09/zamboanga-del-sur.html',
        url + 'mindanao/r09/zamboanga-sibugay.html',
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

        roads = ''

        for p in response.css('.roads-list'):
            roads += "|".join(p.xpath('.//text()').extract())
            # roads = re.sub(r'<.*?>', '', roads)
            # roads = " ".join(roads.split())

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
            'articles': articles.replace(u' ',u' '),
            'roads': roads
        }