__author__ = 'Christina'


import spotipy
import string


## Input text from command line and remove punctuation marks.
poem = raw_input("Please enter poem: ")
cleanpoem = poem.translate(string.maketrans("",""), string.punctuation)


## Split poem into sepearte words to for a list (wordlist).
wordlist = cleanpoem.split()


### Search Spotify Metadata API for track matches to each item in cleanpoem array/list.
 """Needs work."""

spotify = spotipy.Spotify()

for word in wordlist:
    results = spotipy.search(q='track: ' + track, type='track')
    items = results['track']['spotify']
    if len(items) > 0:
        track = items[0]
        pprint.pprint(track['external_urls']['spotify'])
    else:
        print("Sorry, no matches found.")
