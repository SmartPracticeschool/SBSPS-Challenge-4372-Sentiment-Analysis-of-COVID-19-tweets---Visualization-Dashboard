import tweepy
from textblob import TextBlob

API_key = 'kT0SHltK17WYZEqaucLWLY542' 
API_secret_key = 'LJTTvJcriY6n17bTnGMLmHKFK18ZmG3kL8CKctsXvLBfZ6Tz2S'
Access_token = '1030484740846104580-BHcef3brqWSNIj9mAARUooi0uDPitI'
Access_token_secret = 'oVpOa3OkpMukgdG9MqBiiO5vHxZ8CkdhAWyOkfU8ixKtS'

auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(Access_token, Access_token_secret)

api = tweepy.API(auth)



file = open('data.txt', 'w')
file_2 = open('analysis.txt','w')
n = 0
p = 0
v_p = 0
neg = 0
v_neg = 0
neu = 0
tweets_1 = tweepy.Cursor(api.search, q = 'COVID-19').items(1000)
for tweet in tweets_1:
    n += 1
    s = TextBlob(tweet.text).sentiment.polarity
    file_2.write(str(s))
    file_2.write('\n')
    s = float(s)
    if s > 0:
        if s < 0.5:
            p += 1
        else:
            v_p += 1
    elif s < 0:
        if s > -0.5:
            neg += 1
        else:
            v_neg += 1
    else:
        neu += 1
    file.write(str(n))
    file.write('] ')
    file.write(tweet.text)
    file.write('\n\n')
file_2.write('Very-Positive = ')
file_2.write(str/(v_p))
file_2.write('Positive = ')
file_2.write(str/(p))
file_2.write('Neutral = ')
file_2.write(str/(neu))
file_2.write('Negative = ')
file_2.write(str/(neg))
file_2.write('Very-Negative = ')
file_2.write(str/(v_neg))

print('Very-Positive = ', v_p)
print('Positive = ', p)
print('Neutral = ', neu)
print('Negative = ', neg)
print('Very-Negative = ', v_neg)