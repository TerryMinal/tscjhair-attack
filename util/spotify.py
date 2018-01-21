import spotipy
token = "BQCIC3mVpCgwW7bt4iCLDjYOOyYMS6B5wCG8-4KWSXKPv7N1cTqsusgDaYTOhyAQNYZJziODTxR4SG1FC6O1r9BWouipluGz0rrtCh_Suoz6m-DKdM0L-0IxUx_OLSkX6zf_-fUnwavCpiS1Kx4AavVCcY-GvFdaUxkAPQv5CdtEw4jFb6EZ0O00PQ"
def get_tags_from_artist(artist):
    spotify = spotipy.Spotify(auth=token)
    results = spotify.search(q='artist:' + artist, type='artist')
    print (results)
    for song in results['artists']['items']:#['genres']:
        print (song['genres'])
get_tags_from_artist("Two Steps From Hell")
