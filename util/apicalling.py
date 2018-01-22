import urllib
import urllib2
import json
# NOTE: MUST PIP INSTALL CLARIFAI


def getKey(filename):
    try:
        f = open(filename)
        key = f.read()
        return key.strip() #Removes Whitespace
    except Exception as e:
        print "****API KEY NOT FOUND******"
        return ""

def getty(answer):
    answer = urllib.quote(answer)
    url = urllib2.Request("https://api.gettyimages.com/v3/search/images?sort_order=most_popular&phrase=" + answer, headers={ 'Api-Key' : "w7m3fv5uw7kjcz83r37fcwkq"})# getKey("gettykey.txt")})
    uResp = urllib2.urlopen( url )
    contentsraw = uResp.read()
    dat = json.loads(contentsraw)
    if len(dat['images']) == 0:
        return "https://rlv.zcache.com/sad_smiley_face_classic_round_sticker-r364e0eed23d248b982dc0b717710afc1_v9wth_8byvr_324.jpg"
    else:
        return dat['images'][0]['display_sizes'][0]['uri'] #outputs a url to the image



print getty("pie and cake")


from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
def clarifai(imgurl):
    app = ClarifaiApp(api_key= "a1ebd75d22034b018f3b542283f07585")#getKey("clarifaikey.txt"))
    model = app.models.get('general-v1.3')
    image = ClImage(url=imgurl)
    attributes = []
    modelret = model.predict([image])["outputs"][0]["data"]["concepts"]
    for i in range(len(modelret)):
        attributes.append(modelret[i]["name"])
    return attributes

print clarifai(getty("pie and cake"))
