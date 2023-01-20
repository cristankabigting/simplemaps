import json

import sqlite3

con = sqlite3.connect("C:\\Users\\Admin\\Desktop\\Philippines.db")

cur = con.cursor()

jsonfile = open("C:\\Users\\Admin\\Desktop\\Scrapy\\NCRCity\\ncrcity.json")

jsondata = json.load(jsonfile)

data = []

for i in jsondata:

	geotype = i["geotype"].encode('cp1252').decode('utf-8')
	locationname = i["locationname"].encode('cp1252').decode('utf-8')
	islandgroup = i["islandgroup"].encode('cp1252').decode('utf-8')
	regionname = i["regionname"].encode('cp1252').decode('utf-8')
	barangayCount = i["barangayCount"].encode('cp1252').decode('utf-8')
	coastal = i["coastal"].encode('cp1252').decode('utf-8')
	marine = i["marine"].encode('cp1252').decode('utf-8')
	majorisland = i["majorisland"].encode('cp1252').decode('utf-8')
	area = i["area"].encode('cp1252').decode('utf-8')
	population = i["population"].encode('cp1252').decode('utf-8')
	density = i["density"].encode('cp1252').decode('utf-8')
	coordinates = i["coordinates"].encode('cp1252').decode('utf-8').replace("(","")
	elevation = i["elevation"].encode('cp1252').decode('utf-8') 
	latitude = i["latitude"].encode('cp1252').decode('utf-8') 
	longitude = i["longitude"].encode('cp1252').decode('utf-8') 
	nlgu = i["nlgu"].encode('cp1252').decode('utf-8')
	nplace = i["nplace"].encode('cp1252').decode('utf-8')
	distmanila = i["distmanila"].encode('cp1252').decode('utf-8')
	articles = i["articles"].encode('cp1252').decode('utf-8')

	data.append((

		geotype,
		locationname,
		islandgroup,
		regionname,
		barangayCount,
		coastal,
		marine,
		majorisland,
		area,
		population,
		density,
		coordinates,
		elevation,
		latitude,
		longitude,
		nlgu,
		nplace,
		distmanila,
		articles)) 

cur.executemany("INSERT INTO NCRCity VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",data)

con.commit()
  
# Closing file
jsonfile.close()
con.close()