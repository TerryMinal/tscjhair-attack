import spotipy
token = "BQAIKmm11cPE4eTchjAK155riKD06HdArP9OeK0kyrYke_nQ_h-UDKa9vqDJczlPZvGuQHXkNwUvzkotNQwP_Z__e2uyFIn8ny8bvXCIGrEp3m2IvCEpwUK1-K_kyzPNbRB2TVsO0uC_F5_eR8y6kg-KFKL60VFzsx-FXxctO4DxbVRyJOv0HwVCDQ"
def get_tags_from_artist(artist):
    spotify = spotipy.Spotify(auth=token)
    results = spotify.search(q='artist:' + artist, type='artist')
    print (results)
    #print (results['artists']['items'][0]['genres'])
    for song in results['artists']['items']:#['genres']:
    #    print (key)
        print (song['genres'])
        #for key2 in results['artists']['genres'][key]:
        #    print ("\t" + key2)
get_tags_from_artist("Two Steps From Hell")
