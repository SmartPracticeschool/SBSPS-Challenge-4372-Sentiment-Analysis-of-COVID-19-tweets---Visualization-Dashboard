import numpy as np
from PIL import Image # if you don't have it, you'll need to install it

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# We'll be generating word cloud for this text; triple quotes for multi-line string
file = open('data.txt','r')
text = file.read()

wordcloud = WordCloud().generate(text)#install library wordcloud if dont have it

plt.figure() 
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
