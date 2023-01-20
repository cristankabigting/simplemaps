import os

import json

import sqlite3

con = sqlite3.connect("C:\\Users\\Admin\\Desktop\\Philippines.db")

cur = con.cursor()

dirname = 'C:\\Users\\Admin\\Desktop\\Scrapy\\PBarangay'

ext = ('.jsons')

ctr = 0;

for files in os.listdir(dirname):
	if files.endswith(ext):
		print(dirname + '\\' + files)  # printing file name of desired extension
		jsonfile = open(dirname + '\\' + files)
		jsondata = json.load(jsonfile)
		data = []
		for i in jsondata:
			ctr = ctr + 1
			print("Count : %2d" % (ctr))
			geotype = i["geotype"].encode('cp1252').decode('utf-8')
			locationname = i["locationname"].encode('cp1252').decode('utf-8')
			islandgroup = i["islandgroup"].encode('cp1252').decode('utf-8')
			regionname = i["regionname"].encode('cp1252').decode('utf-8')
			provincename = i["provincename"].encode('cp1252').decode('utf-8')
			cityname = i["cityname"].encode('cp1252').decode('utf-8')
			municipalityname = i["municipalityname"].encode('cp1252').decode('utf-8')
			postalcode = i["postalcode"].encode('cp1252').decode('utf-8')
			population = i["population"].encode('cp1252').decode('utf-8')
			majorisland = i["majorisland"].encode('cp1252').decode('utf-8')
			coordinates = i["coordinates"].encode('cp1252').decode('utf-8').replace("(","")
			elevation = i["elevation"].encode('cp1252').decode('utf-8') 
			latitude = i["latitude"].encode('cp1252').decode('utf-8') 
			longitude = i["longitude"].encode('cp1252').decode('utf-8') 
			articles = i["articles"].encode('cp1252').decode('utf-8')
			adjacentbrgy = ' | '.join(map(str, i["adjacentbrgy"]))

			data.append((
				geotype,
				locationname,
				islandgroup,
				regionname,
				provincename,
				cityname,
				municipalityname,
				postalcode,
				population,
				majorisland,
				coordinates,
				elevation,
				latitude,
				longitude,
				articles,
				adjacentbrgy)) 
		cur.executemany("INSERT INTO Barangay VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",data)
		con.commit()
		jsonfile.close()
	else:
		continue

# Closing file
con.close()