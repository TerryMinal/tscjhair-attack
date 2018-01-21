import requests

token = "BQCx-UVRk2wVsctUXGdaFVn6O4J61Hv50iPDKFsZa3Mt4h_y-FbrJbAWJlxkyk3AbVRs1nWdGiPdxuxTCUZPcoQQVJ2ro9-9GpMiWolNNJQ9I46OQnxNqNGFFjqgPuMmaYyH5oLl8RfjCt-uJFwAcCUq1ee49TJs35uYxTfYf1-8G-U2pEfHQ6B-QA"

def get_random(start): #Doesn't work very well
    print 'test'
    req="https://api.spotify.com/v1/search?q="+ start +"&type=artist&offset=20&access_token=" + token
    r = requests.get(req)
    print 'ing'
    j = r.json()['artists']['items']
    print j
    ret = []
    for song in j:
        if song['genres'] != []:
            ret.append(song)
    return ret


def get_artist(code): #You need to get the track ID
    req = "https://api.spotify.com/v1/artists/" + code +"?access_token=" + token
    r = requests.get(req)
    print r.json()['genres']
    print req

def get_song(code): #Doesn't include genres
    req = "https://api.spotify.com/v1/tracks/" + code +"?access_token=" + token
    r = requests.get(req)
    return r.json()#['genres']

def get_relevant_from_random():
    rand = get_random('code')
    rands = []
    for song in rand:
        #You can use href to find more stuff, the rest are needed for catigorazation
        rands.append({'genres':song['genres'], 'name': song['name'], 'href':song['href']})
    return rands

#get_random('two')
#get_artist('2qvP9yerCZCS0U1gZU8wYp')
#get_song("27l2hfl85KUIK9z6N8dNUP")
get_relevant_from_random()
