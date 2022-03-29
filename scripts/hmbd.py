from distutils.command.config import config
import json
import requests
import os


configFile = open(os.path.dirname(__file__)+ '/scriptsConfig.json')
configData = json.load(configFile)

userKey = "&userkey=" + configData['userKey']
piedmontParkPoint = "&lat=33.7884801&Lon=-84.368617"

# step 2: get data from api
getUrl = "https://www.hmdb.org/m.asp?m=64905"
nearbyUrl = "https://www.hmdb.org/db/getnearby.asp?range=5"

getHeaders = {}

requestUrl = nearbyUrl + piedmontParkPoint + userKey

getResponse = requests.get(requestUrl, headers=getHeaders)

xmlDoc = getResponse.content

for i in range(0, 5):
    title = ""

print("Done")
