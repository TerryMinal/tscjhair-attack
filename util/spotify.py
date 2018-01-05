import spotipy
token = ""
def get_tags_from_artist(artist):
    spotify = spotipy.Spotify(auth=token)
    results = spotify.search(q='artist:' + artist, type='artist')
    print (results)
    for song in results['artists']['items']:#['genres']:
        print (song['genres'])
get_tags_from_artist("Two Steps From Hell")
