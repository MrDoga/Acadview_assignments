#Q2 Get ip address of come common site by dns look up
import socket #socket module provides an easy way to look up a host name's ip address

addr1 = socket.gethostbyname('google.com') #used for getting up address
addr2 = socket.gethostbyname('yahoo.com')

print(addr1, addr2)#printing ip address

#Q1 what is access token?generate access token for an api

#access token is a credential that can be used by an application to access an API
#it can be of any type of token and is meant for an API
#the main purpose of these tokens are to tell/inform API that the bearer of the token has been authorized
#to accessa API and to perform specific action

#Q3 Using Tweepy library try to extract tweets from Twitter

import tweepy
from tweepy import Stream #import stream from tweepy lib
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'csERsnfQFwzcirbZ7qyGuQi1k'
csecret = 'TuoOyqhY5M0OilFYENqpm4fhW8LxB9DMdkp6SkMmhXhl3dpRv9'
atoken = '1012068981845286912-jKoRI9XUdVi0QOLkSOVVsQ99bGT5vR'
asecret = 'eEQFBGAlOMMOI1SDBLJes80TARi9q9xooVKarq5UEzIvf'

class listener(StreamListener):
    def on_data(self,data):#on data on air
        print data #print the data
        return True
    def on_error(self,status): #if its not true
        print status
auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track=("car"))

#Q4

#A library contain re-usable chunks of code
#These re-usable codes of library is linked to your program through API
#Api is interface to library through which re-usable codes are linked to an application program

#Q5

#below program plays top 10 tracks of led zeppelin
import spotipy

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp' #token for tope 10 songs of led zepplin

spotify = spotipy.Spotify()
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print 'track    : ' + track['name']
    print 'audio    : ' + track['preview_url']
    print 'cover art: ' + track['album']['images'][0]['url']
    print