import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6,3), subplot_kw=dict(aspect="equal"))

sentiments = ["26 Very-Negative",
            "104 Negative",
            "592 Neutral",
            "328 Positive",
            "40 Very-Positive"]

data = [float(x.split()[0]) for x in sentiments]
count = [x.split()[0] for x in sentiments]
explode = (0, 0, 0.05, 0, 0)
colors = ('darkgreen','forestgreen','lime','forestgreen','darkgreen')

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d} count)".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data,explode=explode,
                                  autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"),
                                  colors = colors)

ax.legend(wedges,
          count,
          title="Sentiment Category",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("SENTIMENT ANALYSIS : COVID-19")

plt.show()
