import numpy as np
from PIL import Image # if you don't have it, you'll need to install it

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# We'll be generating word cloud for this text; triple quotes for multi-line string
file = open('data.txt','r')
text = file.read()

wordcloud = WordCloud().generate(text)

witcher_mask = np.array(Image.open("//home//supercomputer//Desktop//wordcloud//logo.jpeg"))
witcher_mask.shape

wc_2 = WordCloud(background_color="white", mask = witcher_mask, width = witcher_mask.shape[0], height = witcher_mask.shape[1]).generate(text)

# Generating colors from image
image_colors = ImageColorGenerator(witcher_mask)

# show
plt.figure(figsize=[20,15]) # height, width in inches
plt.imshow(wc_2.recolor(color_func=image_colors), interpolation ='bilinear') # Using the color function here
plt.axis("off")
plt.show()
'''
# Display the generated image:
plt.figure() 
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()'''