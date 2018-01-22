import urllib
import urllib2
import json
# NOTE: MUST PIP INSTALL CLARIFAI

SPOTIFY_KEY = ''
GETTY_KEY = ''
CLARIFAI_KEY = ''

def getKey(l='../credentials.txt'):
    try:
        d = {}
        with open(l, "rU") as f: #uses absolute path given
            for line in f:
                a = line.strip().replace(" ", "").split(":")
                # first gets rid of any leading/trailing characters, then gets rid of all whitesplace, then makes
                # list with name of API and API key
                d[a[0]] = a[1] # makes list into dictionary with format {API NAME: API KEY}

            # print d
            global SPOTIFY_KEY
            SPOTIFY_KEY = d["SPOTIFY"]
            global GETTY_KEY
            GETTY_KEY = d["GETTYIMAGES"]
            global CLARIFAI_KEY
            CLARIFAI_KEY = d["CLARIFAI"]
    except Exception as e:
        print "****API KEY NOT FOUND******"
        return ""

# getKey()
# print "GETTY:", GETTY_KEY
# print CLARIFAI_KEY

def getty(answer):
    global GETTY_KEY
    answer = urllib.quote(answer)
    url = urllib2.Request("https://api.gettyimages.com/v3/search/images?sort_order=most_popular&phrase=" + answer, headers={ 'Api-Key' : GETTY_KEY})# getKey("gettykey.txt")})
    uResp = urllib2.urlopen( url )
    contentsraw = uResp.read()
    dat = json.loads(contentsraw)
    if len(dat['images']) == 0:
        return "https://rlv.zcache.com/sad_smiley_face_classic_round_sticker-r364e0eed23d248b982dc0b717710afc1_v9wth_8byvr_324.jpg"
    else:
        return dat['images'][0]['display_sizes'][0]['uri'] #outputs a url to the image



# print getty("pie and cake")


from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
def clarifai(imgurl):
    global CLARIFAI_KEY
    app = ClarifaiApp(api_key= CLARIFAI_KEY)#getKey("clarifaikey.txt"))
    model = app.models.get('general-v1.3')
    image = ClImage(url=imgurl)
    attributes = []
    modelret = model.predict([image])["outputs"][0]["data"]["concepts"]
    for i in range(len(modelret)):
        attributes.append(modelret[i]["name"])
    return attributes

# print clarifai(getty("pie and cake"))
