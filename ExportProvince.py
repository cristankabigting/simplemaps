import json

import sqlite3

con = sqlite3.connect("C:\\Users\\Admin\\Desktop\\Philippines.db")

cur = con.cursor()

jsonfile = open("C:\\Users\\Admin\\Desktop\\Scrapy\\ProvinceSpider\\province.json")

jsondata = json.load(jsonfile)

data = []

for i in jsondata:

	geotype = i["geotype"].encode('cp1252').decode('utf-8')
	locationname = i["locationname"].encode('cp1252').decode('utf-8')
	islandgroup = i["islandgroup"].encode('cp1252').decode('utf-8')
	provinceCount = ""
	cityCount = i["cityCount"].encode('cp1252').decode('utf-8')
	municipalityCount = i["municipalityCount"].encode('cp1252').decode('utf-8')
	barangayCount = i["barangayCount"].encode('cp1252').decode('utf-8')
	coastal = i["coastal"].encode('cp1252').decode('utf-8')
	marine = i["marine"].encode('cp1252').decode('utf-8')
	area = i["area"].encode('cp1252').decode('utf-8')
	population = i["population"].encode('cp1252').decode('utf-8')
	density = i["density"].encode('cp1252').decode('utf-8')
	articles = i["articles"].encode('cp1252').decode('utf-8')
	roads = i["roads"].encode('cp1252').decode('utf-8')
	
	data.append((
		geotype,
		locationname,
		islandgroup,
		provinceCount,
		cityCount,
		municipalityCount,
		barangayCount,
		coastal,
		marine,
		area,
		population,
		density,
		articles,
		roads
		)) 

cur.executemany("INSERT INTO Province VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",data)

con.commit()
  
# Closing file
jsonfile.close()
con.close()