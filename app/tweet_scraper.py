import tweepy

# Inserisci qui le tue credenziali di Twitter
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

def authenticate_twitter():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

def search_tweets(query, count=10, language='en'):
    api = authenticate_twitter()
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang=language, tweet_mode='extended').items(count)
    
    tweet_texts = [tweet.full_text for tweet in tweets]
    
    return tweet_texts