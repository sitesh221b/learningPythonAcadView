import tweepy
import spotipy

#       QUESTION 1

print('An Access Token is an object encapsulating the security identity of a process or thread. The information in a' +
      'token includes the identity and privileges of the user account associated with the process or thread')


#       QUESTION 2

print('Enter the following command in Command Prompt')
print('nslookup www.google.com')
print('nslookup www.facebook.com')


#       QUESTION 3

consumer_key = "KXGkO2Bzesik0AFJnjCDpTm9X"
consumer_secret = "VNNP0vTneYPp325s3jPUdMWkQillH6iyZ3mYmv7FcoMVpVL91M"
access_key = "842271726855585792-lNkFuta9uym1AsOTzG0XAEDVyIG0gAb"
access_secret = "0yJZN6989pqSjcgIozDfhJU1UUnFXvWBEx7mD9jzumcNh"


# Function to extract tweets
def get_tweets(username):

    # Authorization to consumer key & consumer secret
    oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key & access secret
    oauth.set_access_token(access_key, access_secret)

    # Calling API
    api = tweepy.API(oauth)

    tweets = api.user_timeline(screen_name=username)

    tmp = []

    # Create tweet information: username, tweetId, date/time, text
    tweets_in_file = [tweet.text for tweet in tweets]  # CSV File created

    for i in tweets_in_file:
        tmp.append(i)

    print(tmp)
    print(len(tmp))


get_tweets("@iamsrk")


#       QUESTION 4

print('Library: A Library is a collection of functions that serves any particular purpose.')
print('API: An API is an interface for other programs to interact with our program without having direct access')


#       QUESTION 5

katyperry_uri = "spotify:artist:i43hyhchmj8h3bkpvfvzr6i8r"
spotify = spotipy.Spotify()
results = spotify.artist_albums(katyperry_uri, album_type="album")
albums = results['items']

while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])
for album in albums:
    print((album['name']))