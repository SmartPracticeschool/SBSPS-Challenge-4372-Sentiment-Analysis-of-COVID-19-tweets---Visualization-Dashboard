import tweepy

API_key = 'kT0SHltK17WYZEqaucLWLY542' 
API_secret_key = 'LJTTvJcriY6n17bTnGMLmHKFK18ZmG3kL8CKctsXvLBfZ6Tz2S'
Access_token = '1030484740846104580-BHcef3brqWSNIj9mAARUooi0uDPitI'
Access_token_secret = 'oVpOa3OkpMukgdG9MqBiiO5vHxZ8CkdhAWyOkfU8ixKtS'

auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(Access_token, Access_token_secret)

api = tweepy.API(auth)

file = open('data.txt', 'w')
n = 0
tweets_1 = tweepy.Cursor(api.search, q = 'COVID-19').items(1000)
for tweet in tweets_1:
    n += 1
    file.write(str(n))
    file.write('] ')
    file.write(tweet.text)
    file.write('\n\n')
#now the data is collected in the data.txt file
