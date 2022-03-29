from distutils.command.config import config
import json
import requests
import os


configFile = open(os.path.dirname(__file__)+ '/scriptsConfig.json')
configData = json.load(configFile)

userkeyVal = configData['userKey']

# step 2: get data from api
getUrl = "https://www.hmdb.org/m.asp?m=64905"
nearbyUrl = "https://www.hmdb.org/db/getnearby.asp?lat=33.7501965&Lon=-84.3723763&range=5&userkey=" + userkeyVal
piedmontParkUrl = "https://www.hmdb.org/db/getnearby.asp?lat=33.7884801&Lon=-84.368617&range=5&userkey=" + userkeyVal
getHeaders = {}

getResponse = requests.get(nearbyUrl, headers=getHeaders)

xmlDoc = getResponse.content

for i in range(0, 5):
    title = ""

print("Done")
