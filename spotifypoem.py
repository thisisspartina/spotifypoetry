__author__ = 'Christina'


import requests
import requests_cache
import pprint
import string


"""Created a transparent persistent cache for requests."""
requests_cache.install_cache('demo_cache')


## Input text from command line and remove punctuation marks.
poem = raw_input("Please enter poem: ")
cleanpoem = poem.translate(string.maketrans("",""), string.punctuation)

##Split poem into sepearte words to for a list (wordlist)
wordlist = cleanpoem.split()


### Search Spotify Metadata API for track matches to each item in cleanpoem array/list.

"""Working on function, to construct for loop."""
def datacollect(wordlist, playlist):
    r = requests.get('https://api.spotify.com/v1/', params=word)
    pprint.pprint(r.json())
answer = req['tracks']['items'][0]['popularity']
print answer
print req['tracks']['items'][1]['popularity']
