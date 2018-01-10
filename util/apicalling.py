import urllib2
import json

def getKey(filename):
    try:
        f = open(filename)
        key = f.read()
        return key.strip() #Removes Whitespace
    except Exception as e:
        print "****API KEY NOT FOUND******"
        return ""

def getty(answer):
    url = urllib2.Request("https://api.gettyimages.com/v3/search/images?sort_order=most_popular&phrase=" + answer, headers={ 'Api-Key' : getKey("gettykey.txt")})
    uResp = urllib2.urlopen( url )
    contentsraw = uResp.read()
    dat = json.loads(contentsraw)
    if len(dat['images']) == 0:
        return "https://rlv.zcache.com/sad_smiley_face_classic_round_sticker-r364e0eed23d248b982dc0b717710afc1_v9wth_8byvr_324.jpg"
    else:
        return dat['images'][0]['display_sizes'][0]['uri'] #outputs a url to the image



print getty("pie")



from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
def clarifai(img):
    app = ClarifaiApp(api_key=getKey("clarifaikey.txt"))
    model = app.models.get('general-v1.3')
    image = ClImage(url=img)
    model.predict([image])

