import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()

sentiments = ('Very-Negative', 'Negative', 'Neutral', 'Positive', 'Very-Positive')
y_pos = np.arange(len(sentiments))
performance = [26, 104, 592, 238, 40]
error = np.random.rand(len(sentiments))
color = ('darkgreen','forestgreen','lime','forestgreen','darkgreen')

ax.barh(y_pos, performance, xerr=error, align='center',color=color)
ax.set_yticks(y_pos)
ax.set_yticklabels(sentiments)
ax.invert_yaxis()
ax.set_xlabel('Sentiments')
ax.set_title("SENTIMENT ANALYSIS : COVID-19")

plt.show()
