import urllib2
import json

def getKey():
    try:
        f = open("gettykey.txt")
        key = f.read()
        return key.strip() #Removes Whitespace
    except Exception as e:
        print "****API KEY NOT FOUND******"
        return ""

def getty(answer):
    url = urllib2.Request("https://api.gettyimages.com/v3/search/images?sort_order=most_popular&phrase=" + answer, headers={ 'Api-Key' : getKey()})
    uResp = urllib2.urlopen( url )
    contentsraw = uResp.read()
    dat = json.loads(contentsraw)
    return dat

print getty("pie")
