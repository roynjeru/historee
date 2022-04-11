from distutils.command.config import config
import json
import requests
import os
from xml.dom import minidom


configFile = open(os.path.dirname(__file__)+ '/scriptsConfig.json')
configData = json.load(configFile)
userkey = "&userkey=" + configData['userkey']

def getInscription(aID):
    markerUrl = "https://www.hmdb.org/db/getmarker.asp?markerid=" + str(aID) + userkey
    getResponse = requests.get(markerUrl, headers={})

    xmlText = getResponse.text
    parser = minidom.parseString(xmlText)
    hmdbXml = parser.childNodes[1].childNodes

    for i in range(0, hmdbXml.length):
        if (hmdbXml[i].localName == "marker"):
            marker = hmdbXml[i]
            for j in range(0, marker.childNodes.length):
                curAttr = marker.childNodes[j]
                hmdbID = marker._attrs['markerid'].nodeValue
                if(curAttr.localName == "inscription"):
                    return(curAttr.firstChild.data)

def getNearbyPutDB(lat, long):
    point = "&lat=" + str(lat) + "&Lon=" + str(long)
    nearbyUrl = "https://www.hmdb.org/db/getnearby.asp?range=5"

    getHeaders = {}

    requestUrl = nearbyUrl + point + userkey

    getResponse = requests.get(requestUrl, headers=getHeaders)

    xmlText = getResponse.text
    parser = minidom.parseString(xmlText)
    hmdbXml = parser.childNodes[1].childNodes

    for i in range(0, hmdbXml.length):
        if (hmdbXml[i].localName == "marker"):
            marker = hmdbXml[i]
            for j in range(0, marker.childNodes.length):
                curAttr = marker.childNodes[j]
                hmdbID = marker._attrs['markerid'].nodeValue
                mInscription = getInscription(hmdbID)
                if(curAttr.localName == "title"):
                    mTitle = curAttr.firstChild.data
                elif(curAttr.localName == "latitude"):
                    mLatitue = curAttr.firstChild.data
                elif(curAttr.localName == "longitude"):
                    mLongitue = curAttr.firstChild.data
                elif(curAttr.localName == "town"):
                    mTown = curAttr.firstChild.data
                elif(curAttr.localName == "county"):
                    mCounty = curAttr.firstChild.data
                elif(curAttr.localName == "state"):
                    mState = curAttr.firstChild.data
                elif(curAttr.localName == "country"):
                    mCountry = curAttr.firstChild.data
                
            
            print(mTitle, hmdbID, mInscription, mLatitue, mLongitue, mTown, mCounty, mState, mCountry)

if __name__ == '__main__':
    # Piedmont Park: 33.7884801,-84.368617
    getNearbyPutDB(33.7884801, -84.368617)
    # getInscription(17293)