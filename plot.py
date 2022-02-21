import numpy as np
import matplotlib.pyplot as plt

data = [
    [5.337, 2.085, 1.9, 2.977, 1.944, 4.139, 1.618, 1.942, 4.528, 6.348],
    [13.753, 2.890, 2.271, 2.339, 2.215, 6.095, 1.544, 2.363, 6.415, 9.292],
    ]

X = np.arange(10)
fig, ax = plt.subplots()
U1_bar = ax.bar(X       , data[0], color = 'g', width = 0.25)
U2_bar = ax.bar(X + 0.25, data[1], color = 'r', width = 0.25)


ax.set_ylabel('Sekunde')
ax.set_xlabel('Upiti')
ax.set_xticks(X + 0.50 / 2)
ax.set_xticklabels(('I', 'II', 'III', 'Iv', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'))

ax.legend((U1_bar[0], U2_bar[0]), ('prva_v', 'druga_v'))
plt.show()