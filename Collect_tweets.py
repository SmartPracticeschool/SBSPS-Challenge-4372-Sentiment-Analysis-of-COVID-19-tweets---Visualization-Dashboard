import tweepy

API_key = 'kT0SHltK17WYZEqaucLWLY542' 
API_secret_key = 'LJTTvJcriY6n17bTnGMLmHKFK18ZmG3kL8CKctsXvLBfZ6Tz2S'
Access_token = '1030484740846104580-jmLVeqqujDw0xOcgynVOoseXzgImgk'
Access_token_secret = 'cHyuTFjJMvKolgqDTNa8A7qe1jTO8SYLVouNxMnASwEdZ'

auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(Access_token, Access_token_secret)

api = tweepy.API(auth)

'''To collect tweets from different hashtags which are on trending
to get maximum tweets from different places'''

file = open('data.txt', 'w')
n = 0
tweets_1 = tweepy.Cursor(api.search, q = 'coronavirus').items(200)
for tweet in tweets_1:
    n += 1
    file.write(str(n))
    file.write(tweet.text)
    file.write('\n\n')
tweets_2 = tweepy.Cursor(api.search, q = 'covid-19').items(200)
for tweet in tweets_2:
    n += 1
    file.write(str(n))
    file.write(tweet.text)
    file.write('\n\n')
tweets_3 = tweepy.Cursor(api.search, q = 'corona').items(200)
for tweet in tweets_3:
    n += 1
    file.write(str(n))
    file.write(tweet.text)
    file.write('\n\n')
tweets_4 = tweepy.Cursor(api.search, q = 'facesofcovid').items(200)
for tweet in tweets_4:
    n += 1
    file.write(str(n))
    file.write(tweet.text)
    file.write('\n\n')
tweets_5 = tweepy.Cursor(api.search, q = 'coronafights').items(200)
for tweet in tweets_5:
    n += 1
    file.write(str(n))
    file.write(tweet.text)
    file.write('\n\n')

# And now you have collected data in the file data.txt

