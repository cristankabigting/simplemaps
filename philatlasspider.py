import scrapy
import re

class PhilatlasspiderSpider(scrapy.Spider):

    name = 'philatlasspider'

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
        'https://philatlas.com/luzon/r01/ilocos-norte.html',
        'https://philatlas.com/luzon/r01/ilocos-sur.html',
        'https://philatlas.com/luzon/r01/ilocos-norte/adams.html',
        'https://philatlas.com/luzon/ncr/caloocan.html',
        'https://philatlas.com/luzon/r01/ilocos-norte/batac.html',
        'https://philatlas.com/luzon/r02/isabela/santiago.html',
        'https://philatlas.com/mindanao/r11/davao-city.html',
    ]
    
    def parse(self, response):

        locationname = response.xpath('//*[@id="mainHeadWrap"]/h1/text()').extract_first()
        
        geotype = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[2]/td/a/text()').extract_first()
        
        if (geotype == 'region') or (geotype == 'province') or (geotype == 'municipality') or (geotype == 'barangay'):
            print(geotype)           
        else:
            geotype = response.xpath('//*[@id="iboxWrap"]/table/tbody/tr[1]/td/a/text()').extract_first()

        details = ""

        for p in response.css('#popByAgeGrpDet'):
            details += "".join(p.xpath(".//text()").extract())

        articles = "";

        for p in response.css('.articleContent'):

            articles += "".join(p.xpath('.//text()').extract())

            articles = re.sub(r'<.*?>', '', articles)
                
            articles = articles.replace('(adsbygoogle = window.adsbygoogle || []).push({});', '')

            articles = articles.replace('‑', ' to ')

            articles = articles.replace('Maps utilize OpenStreetMap data available under the Open Data Commons Open Database License.(Back to top)', '')

            articles = " ".join(articles.split())

        tablecontent = response.xpath('//*[@id="iboxWrap"]/table')

        for content in tablecontent:

            # geotype = content.xpath('.//tr[2]/td/a/text()').extract()
            
            if (geotype == 'region'):
                islandgroup         = content.xpath('.//tr[3]/td/a/text()').extract_first()
                province_count      = content.xpath('.//tr[4]/td/text()').extract_first()
                city_count          = content.xpath('.//tr[5]/td/text()').extract_first()
                municipality_count  = content.xpath('.//tr[6]/td/text()').extract_first()
                barangay_count      = content.xpath('.//tr[7]/td/text()').extract_first()
                coastaltype         = content.xpath('.//tr[8]/td/text()').extract_first()
                marineboundary      = content.xpath('.//tr[9]/td/text()').extract_first()
                area                = content.xpath('.//tr[10]/td/text()').extract_first()
                population          = content.xpath('.//tr[11]/td/text()').extract_first()
                popdensity          = content.xpath('.//tr[12]/td/text()').extract_first()

                yield {
                    'geotype': geotype.strip(),
                    'locationname': locationname.strip(),
                    'article': articles.strip(),
                    'islandgroup': islandgroup.strip(),
                    'province_count': province_count.strip(),
                    'city_count': city_count.strip(),
                    'municipality_count': municipality_count.strip(),
                    'barangay_count': barangay_count.strip(),
                    'coastaltype': coastaltype.strip(),
                    'marineboundary': marineboundary.strip().replace(u' ',u' '),
                    'area': area.strip(),
                    'population': population.strip(),
                    'popdensity': popdensity.strip()
                }

            elif (geotype == 'province'):
                islandgroup         = content.xpath('.//tr[3]/td/a/text()').extract_first()
                regionname          = content.xpath('.//tr[4]/td/a/text()').extract_first()
                city_count          = content.xpath('.//tr[5]/td/text()').extract_first()
                municipality_count  = content.xpath('.//tr[6]/td/text()').extract_first()
                barangay_count      = content.xpath('.//tr[7]/td/text()').extract_first()
                coastaltype         = content.xpath('.//tr[8]/td/text()').extract_first()
                marineboundary      = content.xpath('.//tr[9]/td/text()').extract_first()
                area                = content.xpath('.//tr[10]/td/text()').extract_first()
                population          = content.xpath('.//tr[11]/td/text()').extract_first()
                popdensity          = content.xpath('.//tr[12]/td/text()').extract_first()
                yield {
                    'geotype': geotype.strip(),
                    'locationname': locationname.strip(),
                    'regionname': regionname.strip().replace(u' ',u' '),
                    'article': articles.strip(),
                    'islandgroup': islandgroup.strip(),
                    'city_count': city_count.strip(),
                    'municipality_count': municipality_count.strip(),
                    'barangay_count': barangay_count.strip(),
                    'coastaltype': coastaltype.strip(),
                    'marineboundary': marineboundary.strip().replace(u' ',u' '),
                    'area': area.strip(),
                    'population': population.strip(),
                    'popdensity': popdensity.strip()
                }

            elif (geotype == 'municipality'):

                islandgroup         = content.xpath('.//tr[2]/td/a/text()').extract_first()
                regionname          = content.xpath('.//tr[3]/td/a/text()').extract_first()
                provincename        = content.xpath('.//tr[4]/td/a/text()').extract_first()
                barangay_count      = content.xpath('.//tr[5]/td/text()').extract_first()
                postalcode          = content.xpath('.//tr[6]/td/text()').extract_first()
                coastaltype         = content.xpath('.//tr[7]/td/text()').extract_first()
                marineboundary      = content.xpath('.//tr[8]/td/text()').extract_first()
                area                = content.xpath('.//tr[10]/td/text()').extract_first()
                population          = content.xpath('.//tr[11]/td/text()').extract_first()
                popdensity          = content.xpath('.//tr[12]/td/text()').extract_first()
                coordinates         = content.xpath('.//tr[13]/td/text()').extract_first()
                latitude            = content.css('#latitude::text').get()
                longitude           = content.css('#longitude::text').get()
                elevation           = content.xpath('.//tr[14]/td/text()').extract_first()

                yield {
                    'geotype': geotype.strip(),
                    'locationname': locationname.strip(),
                    'regionname': regionname.strip().replace(u' ',u' '),
                    'article': articles.strip(),
                    'islandgroup': islandgroup.strip(),
                    'provincename': provincename.strip(),
                    'postalcode': postalcode.strip(),
                    'barangay_count': barangay_count.strip(),
                    'coastaltype': coastaltype.strip(),
                    'marineboundary': marineboundary.strip().replace(u' ',u' '),
                    'area': area.strip(),
                    'population': population.strip(),
                    'popdensity': popdensity.strip(),
                    'latitude': latitude,
                    'longitude': longitude,
                    'coordinates': coordinates.replace(u' ',u' '),
                    'elevation': elevation.replace(u' ',u' ')
                }

            elif (geotype == 'city (highly urbanized)'):

                islandgroup         = content.xpath('.//tr[2]/td/a/text()').extract_first()
                regionname          = content.xpath('.//tr[3]/td/a/text()').extract_first()
                barangay_count      = content.xpath('.//tr[4]/td/text()').extract_first()

                if(regionname == 'National Capital Region (NCR)'):
                    coastaltype         = content.xpath('.//tr[5]/td/text()').extract_first()
                    marineboundary      = content.xpath('.//tr[6]/td/text()').extract_first()
                    majorislandgroup    = content.xpath('.//tr[7]/td/text()').extract_first()
                    area                = content.xpath('.//tr[8]/td/text()').extract_first()
                    population          = content.xpath('.//tr[9]/td/text()').extract_first()
                    popdensity          = content.xpath('.//tr[10]/td/text()').extract_first()
                    coordinates         = content.xpath('.//tr[11]/td/text()').extract_first()
                    latitude            = content.css('#latitude::text').get()
                    longitude           = content.css('#longitude::text').get()
                    elevation           = content.xpath('.//tr[12]/td/text()').extract_first()

                    yield {
                        'geotype': geotype.strip(),
                        'locationname': locationname.strip(),
                        'regionname': regionname.strip().replace(u' ',u' '),
                        'article': articles.strip(),
                        'islandgroup': islandgroup.strip(),
                        'barangay_count': barangay_count.strip(),
                        'coastaltype': coastaltype.strip(),
                        'marineboundary': marineboundary,
                        'area': area.strip(),
                        'population': population.strip(),
                        'popdensity': popdensity.strip(),
                        'latitude': latitude,
                        'longitude': longitude,
                        'coordinates': coordinates.replace(u' ',u' '),
                        'elevation': elevation.replace(u' ',u' ')
                    }

                else:
                    postalcode          = content.xpath('.//tr[5]/td/text()').extract_first()
                    coastaltype         = content.xpath('.//tr[6]/td/text()').extract_first()
                    marineboundary      = content.xpath('.//tr[7]/td/text()').extract_first()
                    majorislandgroup    = content.xpath('.//tr[8]/td/text()').extract_first()
                    area                = content.xpath('.//tr[9]/td/text()').extract_first()
                    population          = content.xpath('.//tr[10]/td/text()').extract_first()
                    popdensity          = content.xpath('.//tr[11]/td/text()').extract_first()
                    coordinates         = content.xpath('.//tr[12]/td/text()').extract_first()
                    latitude            = content.css('#latitude::text').get()
                    longitude           = content.css('#longitude::text').get()
                    elevation           = content.xpath('.//tr[13]/td/text()').extract_first()
                    yield {
                        'geotype': geotype.strip(),
                        'locationname': locationname.strip(),
                        'regionname': regionname.strip().replace(u' ',u' '),
                        'article': articles.strip(),
                        'islandgroup': islandgroup.strip(),
                        'postalcode': postalcode.strip(),
                        'barangay_count': barangay_count.strip(),
                        'coastaltype': coastaltype.strip(),
                        'marineboundary': marineboundary,
                        'area': area.strip(),
                        'population': population.strip(),
                        'popdensity': popdensity.strip(),
                        'latitude': latitude,
                        'longitude': longitude,
                        'coordinates': coordinates.replace(u' ',u' '),
                        'elevation': elevation.replace(u' ',u' ')
                    }


            elif (geotype == 'city (component)'):

                islandgroup         = content.xpath('.//tr[2]/td/a/text()').extract_first()
                regionname          = content.xpath('.//tr[3]/td/a/text()').extract_first()
                provincename        = content.xpath('.//tr[4]/td/a/text()').extract_first()
                barangay_count      = content.xpath('.//tr[5]/td/text()').extract_first()
                postalcode          = content.xpath('.//tr[6]/td/text()').extract_first()
                coastaltype         = content.xpath('.//tr[7]/td/text()').extract_first()
                marineboundary      = content.xpath('.//tr[8]/td/text()').extract_first()
                area                = content.xpath('.//tr[10]/td/text()').extract_first()
                population          = content.xpath('.//tr[11]/td/text()').extract_first()
                popdensity          = content.xpath('.//tr[12]/td/text()').extract_first()
                coordinates         = content.xpath('.//tr[13]/td/text()').extract_first()
                latitude            = content.css('#latitude::text').get()
                longitude           = content.css('#longitude::text').get()
                elevation           = content.xpath('.//tr[14]/td/text()').extract_first()

                yield {
                    'geotype': geotype.strip(),
                    'locationname': locationname.strip(),
                    'regionname': regionname.strip().replace(u' ',u' '),
                    'article': articles.strip(),
                    'islandgroup': islandgroup.strip(),
                    'provincename': provincename.strip(),
                    'postalcode': postalcode.strip(),
                    'barangay_count': barangay_count.strip(),
                    'coastaltype': coastaltype.strip(),
                    'marineboundary': marineboundary.strip().replace(u' ',u' '),
                    'area': area.strip(),
                    'population': population.strip(),
                    'popdensity': popdensity.strip(),
                    'latitude': latitude,
                    'longitude': longitude,
                    'coordinates': coordinates.replace(u' ',u' '),
                    'elevation': elevation.replace(u' ',u' ')
                }

            elif (geotype == 'city (independent component)'):

                islandgroup         = content.xpath('.//tr[2]/td/a/text()').extract_first()
                regionname          = content.xpath('.//tr[3]/td/a/text()').extract_first()
                provincename        = content.xpath('.//tr[4]/td/a/text()').extract_first()
                barangay_count      = content.xpath('.//tr[5]/td/text()').extract_first()
                postalcode          = content.xpath('.//tr[6]/td/text()').extract_first()
                coastaltype         = content.xpath('.//tr[7]/td/text()').extract_first()
                marineboundary      = content.xpath('.//tr[8]/td/text()').extract_first()
                area                = content.xpath('.//tr[10]/td/text()').extract_first()
                population          = content.xpath('.//tr[11]/td/text()').extract_first()
                popdensity          = content.xpath('.//tr[12]/td/text()').extract_first()
                coordinates         = content.xpath('.//tr[13]/td/text()').extract_first()
                latitude            = content.css('#latitude::text').get()
                longitude           = content.css('#longitude::text').get()
                elevation           = content.xpath('.//tr[14]/td/text()').extract_first()

                yield {
                    'geotype': geotype.strip(),
                    'locationname': locationname.strip(),
                    'regionname': regionname.strip().replace(u' ',u' '),
                    'article': articles.strip(),
                    'islandgroup': islandgroup.strip(),
                    'provincename': provincename.strip(),
                    'postalcode': postalcode.strip(),
                    'barangay_count': barangay_count.strip(),
                    'coastaltype': coastaltype.strip(),
                    'marineboundary': marineboundary.strip().replace(u' ',u' '),
                    'area': area.strip(),
                    'population': population.strip(),
                    'popdensity': popdensity.strip(),
                    'latitude': latitude,
                    'longitude': longitude,
                    'coordinates': coordinates.replace(u' ',u' '),
                    'elevation': elevation.replace(u' ',u' ')
                }
