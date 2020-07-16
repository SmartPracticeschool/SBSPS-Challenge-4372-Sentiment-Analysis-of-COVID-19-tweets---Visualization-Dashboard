from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = 'kT0SHltK17WYZEqaucLWLY542'
consumer_secret = 'LJTTvJcriY6n17bTnGMLmHKFK18ZmG3kL8CKctsXvLBfZ6Tz2S'

access_token = '1030484740846104580-CtKmGNwmoCHTFfJPUZ51b2Gk4sAzjA'
access_token_secret = '2cwRg6UOPHe9qWA77J56myaqISVT9oNqhmLOHBeXH5TIh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})

app.run()
