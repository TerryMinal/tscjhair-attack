import requests

token = "BQBbgaJq4E90X6YfIiGQaVFJga_EKuOODw3YEKEsA38m7g7hvnJ5zfL15Gt2_LlFy3sOfv3QY91hjxe0wXzssR9J8evA5X9aLv8PLGoy-HakUFATsv8oJUGaFxRLbERQ6phov7Kv4W3Sl2faouAISr4vyAyPJL2v1ovJ6G74ec9BijgPSjRA4VQGNw"

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

#get_random('two')
get_artist('2qvP9yerCZCS0U1gZU8wYp')
