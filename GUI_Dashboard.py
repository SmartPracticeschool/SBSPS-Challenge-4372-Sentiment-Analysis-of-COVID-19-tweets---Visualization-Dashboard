from tkinter import ttk
from tkinter import *
import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt 
import cv2
import PIL.Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def aaa():
    very_negative = 0
    very_positive = 0
    negative = 0
    positive = 0
    neutral = 0
    values = []
    file = open('data.txt', 'w')

    for i in tweets:
        s = TextBlob(i.text).sentiment.polarity
        file.write(i.text)
        if s > 0:
            if s < 0.5:
                positive += 1
            else:
                very_positive += 1
        elif s < 0:
            if s > -0.5:
                negative += 1
            else:
                very_negative += 1
        else:
            neutral += 1
    file.close()
    values.append(very_positive)
    values.append(positive)
    values.append(neutral)
    values.append(negative)
    values.append(very_negative)

    names = ['very_positive','positive','neutral','negative','very_negative']
    colors = ['g', 'gold', 'b', 'orange', 'r'] 
    plt.pie(values, explode=(0,0,0,0.1,0.2), labels = names, colors = colors, autopct= '%1.1f%%',shadow=True, startangle=90)
    plt.savefig("img.png")
    img = PhotoImage(file = "img.png")
    return img
    
def word_cloud():
    file = open('data.txt','r')
    text = file.read()
    wordcloud = WordCloud().generate(text)
    plt.figure() 
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("cloud.png")
    img_1 = PhotoImage(file = "cloud.png")
    return img_1
    
    
    

if __name__ == "__main__":

    API_key = 'kT0SHltK17WYZEqaucLWLY542' 
    API_secret_key = 'LJTTvJcriY6n17bTnGMLmHKFK18ZmG3kL8CKctsXvLBfZ6Tz2S'
    Access_token = '1030484740846104580-CtKmGNwmoCHTFfJPUZ51b2Gk4sAzjA'
    Access_token_secret = '2cwRg6UOPHe9qWA77J56myaqISVT9oNqhmLOHBeXH5TIh'
    auth = tweepy.OAuthHandler(API_key, API_secret_key)
    auth.set_access_token(Access_token, Access_token_secret)
    api = tweepy.API(auth)
    tweets = tweepy.Cursor(api.search, q = 'COVID-19').items(5)
    
    root = Tk()
    img = aaa()
    img_1 = word_cloud()
    #root.geometry("900x1200")
    w = ttk.Label(root, text ='COVID-19', font = "500")  
    w.pack() 

    p = ttk.Label(root)
    p.pack()
    q = ttk.Label(root)
    q.pack()
    p.config(image = img)
    q.config(image = img_1)

    r = ttk.Button(root, text = "Refresh", command = aaa)
    r.pack()
    
    root.mainloop()
