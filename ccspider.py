import scrapy
import re

class CcspiderSpider(scrapy.Spider):
    
    name = 'ccspider'

    allowed_domains = ['philatlas.com']

    url = 'https://philatlas.com/'

    ext = '.html'

    start_urls = [

        url +  'luzon/r01/pangasinan/alaminos' + ext,
        url +  'luzon/r04a/rizal/antipolo' + ext,
        url +  'luzon/r04a/cavite/bacoor' + ext,
        url +  'visayas/r06/negros-occidental/bago' + ext,
        url +  'visayas/r07/negros-oriental/bais' + ext,
        url +  'luzon/r03/bataan/balanga' + ext,
        url +  'luzon/r01/ilocos-norte/batac' + ext,
        url +  'luzon/r04a/batangas/batangas-city' + ext,
        url +  'visayas/r07/negros-oriental/bayawan' + ext,
        url +  'visayas/r08/leyte/baybay' + ext,
        url +  'mindanao/caraga/agusan-del-sur/bayugan' + ext,
        url +  'mindanao/caraga/surigao-del-sur/bislig' + ext,
        url +  'luzon/r04a/laguna/binan' + ext,
        url +  'visayas/r07/cebu/bogo' + ext,
        url +  'visayas/r08/eastern-samar/borongan' + ext,
        url +  'mindanao/caraga/agusan-del-norte/cabadbaran' + ext,
        url +  'luzon/r03/nueva-ecija/cabanatuan' + ext,
        url +  'luzon/r04a/laguna/cabuyao' + ext,
        url +  'visayas/r06/negros-occidental/cadiz' + ext,
        url +  'luzon/r04a/laguna/calamba' + ext,
        url +  'luzon/mimaropa/oriental-mindoro/calapan' + ext,
        url +  'visayas/r08/samar/calbayog' + ext,
        url +  'luzon/r01/ilocos-sur/candon' + ext,
        url +  'visayas/r07/negros-oriental/canlaon' + ext,
        url +  'visayas/r07/cebu/carcar' + ext,
        url +  'visayas/r08/samar/catbalogan' + ext,
        url +  'luzon/r02/isabela/cauayan' + ext,
        url +  'luzon/r04a/cavite/cavite-city' + ext,
        url +  'visayas/r07/cebu/danao' + ext,
        url +  'mindanao/r09/zamboanga-del-norte/dapitan' + ext,
        url +  'luzon/r04a/cavite/dasmarinas' + ext,
        url +  'mindanao/r11/davao-del-sur/digos' + ext,
        url +  'mindanao/r09/zamboanga-del-norte/dipolog' + ext,
        url +  'visayas/r07/negros-oriental/dumaguete' + ext,
        url +  'mindanao/r10/misamis-oriental/el-salvador' + ext,
        url +  'visayas/r06/negros-occidental/escalante' + ext,
        url +  'luzon/r03/nueva-ecija/gapan' + ext,
        url +  'luzon/r04a/cavite/general-trias' + ext,
        url +  'mindanao/r10/misamis-oriental/gingoog' + ext,
        url +  'visayas/r07/negros-oriental/guihulngan' + ext,
        url +  'visayas/r06/negros-occidental/himamaylan' + ext,
        url +  'luzon/r02/isabela/ilagan' + ext,
        url +  'luzon/r04a/cavite/imus' + ext,
        url +  'luzon/r05/camarines-sur/iriga' + ext,
        url +  'mindanao/r09/isabela-city' + ext,
        url +  'visayas/r06/negros-occidental/kabankalan' + ext,
        url +  'mindanao/r12/cotabato/kidapawan' + ext,
        url +  'mindanao/r12/south-cotabato/koronadal' + ext,
        url +  'visayas/r06/negros-occidental/la-carlota' + ext,
        url +  'mindanao/barmm/basilan/lamitan' + ext,
        url +  'luzon/r01/ilocos-norte/laoag' + ext,
        url +  'luzon/r05/albay/legazpi' + ext,
        url +  'luzon/r05/albay/ligao' + ext,
        url +  'luzon/r04a/batangas/lipa' + ext,
        url +  'visayas/r08/southern-leyte/maasin' + ext,
        url +  'luzon/r03/pampanga/mabalacat' + ext,
        url +  'mindanao/r10/bukidnon/malaybalay' + ext,
        url +  'luzon/r03/bulacan/malolos' + ext,
        url +  'mindanao/barmm/lanao-del-sur/marawi' + ext,
        url +  'luzon/r05/masbate/masbate-city' + ext,
        url +  'mindanao/r11/davao-oriental/mati' + ext,
        url +  'luzon/r03/bulacan/meycauayan' + ext,
        url +  'luzon/r03/nueva-ecija/munoz' + ext,
        url +  'visayas/r07/cebu/naga' + ext,
        url +  'mindanao/r10/misamis-occidental/oroquieta' + ext,
        url +  'mindanao/r10/misamis-occidental/ozamiz' + ext,
        url +  'mindanao/r09/zamboanga-del-sur/pagadian' + ext,
        url +  'luzon/r03/nueva-ecija/palayan' + ext,
        url +  'mindanao/r11/davao-del-norte/panabo' + ext,
        url +  'visayas/r06/iloilo/passi' + ext,
        url +  'visayas/r06/capiz/roxas-city' + ext,
        url +  'visayas/r06/negros-occidental/sagay' + ext,
        url +  'mindanao/r11/davao-del-norte/samal' + ext,
        url +  'luzon/r01/pangasinan/san-carlos' + ext,
        url +  'visayas/r06/negros-occidental/san-carlos' + ext,
        url +  'luzon/r01/la-union/san-fernando' + ext,
        url +  'luzon/r03/pampanga/san-fernando' + ext,
        url +  'luzon/r03/nueva-ecija/san-jose' + ext,
        url +  'luzon/r03/bulacan/san-jose-del-monte' + ext,
        url +  'luzon/r04a/laguna/san-pablo' + ext,
        url +  'luzon/r04a/laguna/san-pedro' + ext,
        url +  'luzon/r04a/laguna/santa-rosa' + ext,
        url +  'luzon/r04a/batangas/santo-tomas' + ext,
        url +  'visayas/r06/negros-occidental/silay' + ext,
        url +  'visayas/r06/negros-occidental/sipalay' + ext,
        url +  'luzon/r05/sorsogon/sorsogon-city' + ext,
        url +  'mindanao/caraga/surigao-del-norte/surigao-city' + ext,
        url +  'luzon/r05/albay/tabaco' + ext,
        url +  'luzon/car/kalinga/tabuk' + ext,
        url +  'mindanao/r12/sultan-kudarat/tacurong' + ext,
        url +  'luzon/r04a/cavite/tagaytay' + ext,
        url +  'visayas/r07/bohol/tagbilaran' + ext,
        url +  'mindanao/r11/davao-del-norte/tagum' + ext,
        url +  'visayas/r06/negros-occidental/talisay' + ext,
        url +  'visayas/r07/cebu/talisay' + ext,
        url +  'luzon/r04a/batangas/tanauan' + ext,
        url +  'mindanao/caraga/surigao-del-sur/tandag' + ext,
        url +  'mindanao/r10/misamis-occidental/tangub' + ext,
        url +  'visayas/r07/negros-oriental/tanjay' + ext,
        url +  'luzon/r03/tarlac/tarlac-city' + ext,
        url +  'luzon/r04a/quezon/tayabas' + ext,
        url +  'visayas/r07/cebu/toledo' + ext,
        url +  'luzon/r04a/cavite/trece-martires' + ext,
        url +  'luzon/r02/cagayan/tuguegarao' + ext,
        url +  'luzon/r01/pangasinan/urdaneta' + ext,
        url +  'mindanao/r10/bukidnon/valencia' + ext,
        url +  'visayas/r06/negros-occidental/victorias' + ext,
        url +  'luzon/r01/ilocos-sur/vigan' + ext
    ]

    def parse(self, response):
        locationname = response.xpath('//*[@id="mainHeadWrap"]/h1/text()').get()
        geotype = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[1]/td/a/text()').get()
        islandgroup = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[2]/td/a/text()').get()
        regionname = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[3]/td/a/text()').get()
        if locationname == 'Isabela City':
            provincename = 'Basilan'    
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