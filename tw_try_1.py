import csv
import tweepy
import ssl

consumer_key = "**"
consumer_secret = "**"
access_token = "**"
access_token_secret = "**"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
ssl._create_default_https_context = ssl._create_unverified_context
api = tweepy.API(auth)
api = tweepy.API(auth, wait_on_rate_limit=True)

user = api.verify_credentials()
print (user.name)

name = '**'
tweet_id = '**'

replies=[]
for tweet in tweepy.Cursor(api.search_tweets,q=name, result_type='recent').items(10):
    print(tweet.text)
    replies.append(tweet.text)


for tweet in tweepy.Cursor(api.search_tweets,q='to:'+name, result_type='recent').items(100):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
        if (tweet.in_reply_to_status_id_str==tweet_id):
            replies.append(tweet)


for tweet in replies:
        row = {'user': tweet.user.screen_name, 'text': tweet.text.replace('\n', ' ')}
        print(row)

